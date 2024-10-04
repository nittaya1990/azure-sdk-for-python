# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE.txt in the project root for
# license information.
# -------------------------------------------------------------------------
import time
import base64
from typing import TYPE_CHECKING, Optional, TypeVar, MutableMapping, Any, Union, cast
from azure.core.credentials import (
    TokenCredential,
    SupportsTokenInfo,
    TokenRequestOptions,
    TokenProvider,
)
from azure.core.pipeline import PipelineRequest, PipelineResponse
from azure.core.pipeline.transport import (
    HttpResponse as LegacyHttpResponse,
    HttpRequest as LegacyHttpRequest,
)
from azure.core.rest import HttpResponse, HttpRequest
from . import HTTPPolicy, SansIOHTTPPolicy
from ...exceptions import ServiceRequestError
from ._utils import get_challenge_parameter

if TYPE_CHECKING:

    from azure.core.credentials import (
        AccessToken,
        AccessTokenInfo,
        AzureKeyCredential,
        AzureSasCredential,
    )

HTTPResponseType = TypeVar("HTTPResponseType", HttpResponse, LegacyHttpResponse)
HTTPRequestType = TypeVar("HTTPRequestType", HttpRequest, LegacyHttpRequest)


# pylint:disable=too-few-public-methods
class _BearerTokenCredentialPolicyBase:
    """Base class for a Bearer Token Credential Policy.

    :param credential: The credential.
    :type credential: ~azure.core.credentials.TokenProvider
    :param str scopes: Lets you specify the type of access needed.
    :keyword bool enable_cae: Indicates whether to enable Continuous Access Evaluation (CAE) on all requested
        tokens. Defaults to False.
    """

    def __init__(self, credential: TokenProvider, *scopes: str, **kwargs: Any) -> None:
        super(_BearerTokenCredentialPolicyBase, self).__init__()
        self._scopes = scopes
        self._credential = credential
        self._token: Optional[Union["AccessToken", "AccessTokenInfo"]] = None
        self._enable_cae: bool = kwargs.get("enable_cae", False)

    @staticmethod
    def _enforce_https(request: PipelineRequest[HTTPRequestType]) -> None:
        # move 'enforce_https' from options to context so it persists
        # across retries but isn't passed to a transport implementation
        option = request.context.options.pop("enforce_https", None)

        # True is the default setting; we needn't preserve an explicit opt in to the default behavior
        if option is False:
            request.context["enforce_https"] = option

        enforce_https = request.context.get("enforce_https", True)
        if enforce_https and not request.http_request.url.lower().startswith("https"):
            raise ServiceRequestError(
                "Bearer token authentication is not permitted for non-TLS protected (non-https) URLs."
            )

    @staticmethod
    def _update_headers(headers: MutableMapping[str, str], token: str) -> None:
        """Updates the Authorization header with the bearer token.

        :param MutableMapping[str, str] headers: The HTTP Request headers
        :param str token: The OAuth token.
        """
        headers["Authorization"] = "Bearer {}".format(token)

    @property
    def _need_new_token(self) -> bool:
        now = time.time()
        refresh_on = getattr(self._token, "refresh_on", None)
        return not self._token or (refresh_on and refresh_on <= now) or self._token.expires_on - now < 300

    def _get_token(self, *scopes: str, **kwargs: Any) -> Union["AccessToken", "AccessTokenInfo"]:
        if self._enable_cae:
            kwargs.setdefault("enable_cae", self._enable_cae)

        if hasattr(self._credential, "get_token_info"):
            options: TokenRequestOptions = {}
            # Loop through all the keyword arguments and check if they are part of the TokenRequestOptions.
            for key in list(kwargs.keys()):
                if key in TokenRequestOptions.__annotations__:  # pylint: disable=no-member
                    options[key] = kwargs.pop(key)  # type: ignore[literal-required]

            return cast(SupportsTokenInfo, self._credential).get_token_info(*scopes, options=options)
        return cast(TokenCredential, self._credential).get_token(*scopes, **kwargs)

    def _request_token(self, *scopes: str, **kwargs: Any) -> None:
        """Request a new token from the credential.

        This will call the credential's appropriate method to get a token and store it in the policy.

        :param str scopes: The type of access needed.
        """
        self._token = self._get_token(*scopes, **kwargs)


class BearerTokenCredentialPolicy(_BearerTokenCredentialPolicyBase, HTTPPolicy[HTTPRequestType, HTTPResponseType]):
    """Adds a bearer token Authorization header to requests.

    :param credential: The credential.
    :type credential: ~azure.core.TokenCredential
    :param str scopes: Lets you specify the type of access needed.
    :keyword bool enable_cae: Indicates whether to enable Continuous Access Evaluation (CAE) on all requested
        tokens. Defaults to False.
    :raises: :class:`~azure.core.exceptions.ServiceRequestError`
    """

    def on_request(self, request: PipelineRequest[HTTPRequestType]) -> None:
        """Called before the policy sends a request.

        The base implementation authorizes the request with a bearer token.

        :param ~azure.core.pipeline.PipelineRequest request: the request
        """
        self._enforce_https(request)

        if self._token is None or self._need_new_token:
            self._request_token(*self._scopes)
        bearer_token = cast(Union["AccessToken", "AccessTokenInfo"], self._token).token
        self._update_headers(request.http_request.headers, bearer_token)

    def authorize_request(self, request: PipelineRequest[HTTPRequestType], *scopes: str, **kwargs: Any) -> None:
        """Acquire a token from the credential and authorize the request with it.

        Keyword arguments are passed to the credential's get_token method. The token will be cached and used to
        authorize future requests.

        :param ~azure.core.pipeline.PipelineRequest request: the request
        :param str scopes: required scopes of authentication
        """
        self._request_token(*scopes, **kwargs)
        bearer_token = cast(Union["AccessToken", "AccessTokenInfo"], self._token).token
        self._update_headers(request.http_request.headers, bearer_token)

    def send(self, request: PipelineRequest[HTTPRequestType]) -> PipelineResponse[HTTPRequestType, HTTPResponseType]:
        """Authorize request with a bearer token and send it to the next policy

        :param request: The pipeline request object
        :type request: ~azure.core.pipeline.PipelineRequest
        :return: The pipeline response object
        :rtype: ~azure.core.pipeline.PipelineResponse
        """
        self.on_request(request)
        try:
            response = self.next.send(request)
        except Exception:
            self.on_exception(request)
            raise

        self.on_response(request, response)
        if response.http_response.status_code == 401:
            self._token = None  # any cached token is invalid
            if "WWW-Authenticate" in response.http_response.headers:
                request_authorized = self.on_challenge(request, response)
                if request_authorized:
                    # if we receive a challenge response, we retrieve a new token
                    # which matches the new target. In this case, we don't want to remove
                    # token from the request so clear the 'insecure_domain_change' tag
                    request.context.options.pop("insecure_domain_change", False)
                    try:
                        response = self.next.send(request)
                        self.on_response(request, response)
                    except Exception:
                        self.on_exception(request)
                        raise

        return response

    def on_challenge(
        self,
        request: PipelineRequest[HTTPRequestType],
        response: PipelineResponse[HTTPRequestType, HTTPResponseType],
    ) -> bool:
        """Authorize request according to an authentication challenge

        This method is called when the resource provider responds 401 with a WWW-Authenticate header.

        :param ~azure.core.pipeline.PipelineRequest request: the request which elicited an authentication challenge
        :param ~azure.core.pipeline.PipelineResponse response: the resource provider's response
        :returns: a bool indicating whether the policy should send the request
        :rtype: bool
        """
        # pylint:disable=unused-argument
        headers = response.http_response.headers
        error = get_challenge_parameter(headers, "Bearer", "error")
        if error == "insufficient_claims":
            encoded_claims = get_challenge_parameter(headers, "Bearer", "claims")
            if not encoded_claims:
                return False
            try:
                padding_needed = -len(encoded_claims) % 4
                claims = base64.urlsafe_b64decode(encoded_claims + "=" * padding_needed).decode("utf-8")
                if claims:
                    token = self._get_token(*self._scopes, claims=claims)
                    bearer_token = cast(Union["AccessToken", "AccessTokenInfo"], token).token
                    request.http_request.headers["Authorization"] = "Bearer " + bearer_token
                    return True
            except Exception:  # pylint:disable=broad-except
                return False
        return False

    def on_response(
        self,
        request: PipelineRequest[HTTPRequestType],
        response: PipelineResponse[HTTPRequestType, HTTPResponseType],
    ) -> None:
        """Executed after the request comes back from the next policy.

        :param request: Request to be modified after returning from the policy.
        :type request: ~azure.core.pipeline.PipelineRequest
        :param response: Pipeline response object
        :type response: ~azure.core.pipeline.PipelineResponse
        """

    def on_exception(self, request: PipelineRequest[HTTPRequestType]) -> None:
        """Executed when an exception is raised while executing the next policy.

        This method is executed inside the exception handler.

        :param request: The Pipeline request object
        :type request: ~azure.core.pipeline.PipelineRequest
        """
        # pylint: disable=unused-argument
        return


class AzureKeyCredentialPolicy(SansIOHTTPPolicy[HTTPRequestType, HTTPResponseType]):
    """Adds a key header for the provided credential.

    :param credential: The credential used to authenticate requests.
    :type credential: ~azure.core.credentials.AzureKeyCredential
    :param str name: The name of the key header used for the credential.
    :keyword str prefix: The name of the prefix for the header value if any.
    :raises: ValueError or TypeError
    """

    def __init__(  # pylint: disable=unused-argument
        self,
        credential: "AzureKeyCredential",
        name: str,
        *,
        prefix: Optional[str] = None,
        **kwargs: Any,
    ) -> None:
        super().__init__()
        if not hasattr(credential, "key"):
            raise TypeError("String is not a supported credential input type. Use an instance of AzureKeyCredential.")
        if not name:
            raise ValueError("name can not be None or empty")
        if not isinstance(name, str):
            raise TypeError("name must be a string.")
        self._credential = credential
        self._name = name
        self._prefix = prefix + " " if prefix else ""

    def on_request(self, request: PipelineRequest[HTTPRequestType]) -> None:
        request.http_request.headers[self._name] = f"{self._prefix}{self._credential.key}"


class AzureSasCredentialPolicy(SansIOHTTPPolicy[HTTPRequestType, HTTPResponseType]):
    """Adds a shared access signature to query for the provided credential.

    :param credential: The credential used to authenticate requests.
    :type credential: ~azure.core.credentials.AzureSasCredential
    :raises: ValueError or TypeError
    """

    def __init__(
        self,  # pylint: disable=unused-argument
        credential: "AzureSasCredential",
        **kwargs: Any,
    ) -> None:
        super(AzureSasCredentialPolicy, self).__init__()
        if not credential:
            raise ValueError("credential can not be None")
        self._credential = credential

    def on_request(self, request: PipelineRequest[HTTPRequestType]) -> None:
        url = request.http_request.url
        query = request.http_request.query
        signature = self._credential.signature
        if signature.startswith("?"):
            signature = signature[1:]
        if query:
            if signature not in url:
                url = url + "&" + signature
        else:
            if url.endswith("?"):
                url = url + signature
            else:
                url = url + "?" + signature
        request.http_request.url = url
