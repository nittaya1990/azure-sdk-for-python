# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, TYPE_CHECKING, Union

from azure.core.credentials import AzureKeyCredential
from azure.core.pipeline import policies

from ._version import VERSION

if TYPE_CHECKING:
    from azure.core.credentials import TokenCredential


class FaceAdministrationClientConfiguration:  # pylint: disable=too-many-instance-attributes
    """Configuration for FaceAdministrationClient.

    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param endpoint: Supported Cognitive Services endpoints (protocol and hostname, for example:
     https://{resource-name}.cognitiveservices.azure.com). Required.
    :type endpoint: str
    :param credential: Credential used to authenticate requests to the service. Is either a
     AzureKeyCredential type or a TokenCredential type. Required.
    :type credential: ~azure.core.credentials.AzureKeyCredential or
     ~azure.core.credentials.TokenCredential
    :keyword api_version: API Version. Known values are "v1.2-preview.1" and None. Default value is
     "v1.2-preview.1". Note that overriding this default value may result in unsupported behavior.
    :paramtype api_version: str or ~azure.ai.vision.face.models.Versions
    """

    def __init__(self, endpoint: str, credential: Union[AzureKeyCredential, "TokenCredential"], **kwargs: Any) -> None:
        api_version: str = kwargs.pop("api_version", "v1.2-preview.1")

        if endpoint is None:
            raise ValueError("Parameter 'endpoint' must not be None.")
        if credential is None:
            raise ValueError("Parameter 'credential' must not be None.")

        self.endpoint = endpoint
        self.credential = credential
        self.api_version = api_version
        self.credential_scopes = kwargs.pop("credential_scopes", ["https://cognitiveservices.azure.com/.default"])
        kwargs.setdefault("sdk_moniker", "ai-vision-face/{}".format(VERSION))
        self.polling_interval = kwargs.get("polling_interval", 30)
        self._configure(**kwargs)

    def _infer_policy(self, **kwargs):
        if isinstance(self.credential, AzureKeyCredential):
            return policies.AzureKeyCredentialPolicy(self.credential, "Ocp-Apim-Subscription-Key", **kwargs)
        if hasattr(self.credential, "get_token"):
            return policies.BearerTokenCredentialPolicy(self.credential, *self.credential_scopes, **kwargs)
        raise TypeError(f"Unsupported credential: {self.credential}")

    def _configure(self, **kwargs: Any) -> None:
        self.user_agent_policy = kwargs.get("user_agent_policy") or policies.UserAgentPolicy(**kwargs)
        self.headers_policy = kwargs.get("headers_policy") or policies.HeadersPolicy(**kwargs)
        self.proxy_policy = kwargs.get("proxy_policy") or policies.ProxyPolicy(**kwargs)
        self.logging_policy = kwargs.get("logging_policy") or policies.NetworkTraceLoggingPolicy(**kwargs)
        self.http_logging_policy = kwargs.get("http_logging_policy") or policies.HttpLoggingPolicy(**kwargs)
        self.custom_hook_policy = kwargs.get("custom_hook_policy") or policies.CustomHookPolicy(**kwargs)
        self.redirect_policy = kwargs.get("redirect_policy") or policies.RedirectPolicy(**kwargs)
        self.retry_policy = kwargs.get("retry_policy") or policies.RetryPolicy(**kwargs)
        self.authentication_policy = kwargs.get("authentication_policy")
        if self.credential and not self.authentication_policy:
            self.authentication_policy = self._infer_policy(**kwargs)


class FaceClientConfiguration:  # pylint: disable=too-many-instance-attributes
    """Configuration for FaceClient.

    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param endpoint: Supported Cognitive Services endpoints (protocol and hostname, for example:
     https://{resource-name}.cognitiveservices.azure.com). Required.
    :type endpoint: str
    :param credential: Credential used to authenticate requests to the service. Is either a
     AzureKeyCredential type or a TokenCredential type. Required.
    :type credential: ~azure.core.credentials.AzureKeyCredential or
     ~azure.core.credentials.TokenCredential
    :keyword api_version: API Version. Known values are "v1.2-preview.1" and None. Default value is
     "v1.2-preview.1". Note that overriding this default value may result in unsupported behavior.
    :paramtype api_version: str or ~azure.ai.vision.face.models.Versions
    """

    def __init__(self, endpoint: str, credential: Union[AzureKeyCredential, "TokenCredential"], **kwargs: Any) -> None:
        api_version: str = kwargs.pop("api_version", "v1.2-preview.1")

        if endpoint is None:
            raise ValueError("Parameter 'endpoint' must not be None.")
        if credential is None:
            raise ValueError("Parameter 'credential' must not be None.")

        self.endpoint = endpoint
        self.credential = credential
        self.api_version = api_version
        self.credential_scopes = kwargs.pop("credential_scopes", ["https://cognitiveservices.azure.com/.default"])
        kwargs.setdefault("sdk_moniker", "ai-vision-face/{}".format(VERSION))
        self.polling_interval = kwargs.get("polling_interval", 30)
        self._configure(**kwargs)

    def _infer_policy(self, **kwargs):
        if isinstance(self.credential, AzureKeyCredential):
            return policies.AzureKeyCredentialPolicy(self.credential, "Ocp-Apim-Subscription-Key", **kwargs)
        if hasattr(self.credential, "get_token"):
            return policies.BearerTokenCredentialPolicy(self.credential, *self.credential_scopes, **kwargs)
        raise TypeError(f"Unsupported credential: {self.credential}")

    def _configure(self, **kwargs: Any) -> None:
        self.user_agent_policy = kwargs.get("user_agent_policy") or policies.UserAgentPolicy(**kwargs)
        self.headers_policy = kwargs.get("headers_policy") or policies.HeadersPolicy(**kwargs)
        self.proxy_policy = kwargs.get("proxy_policy") or policies.ProxyPolicy(**kwargs)
        self.logging_policy = kwargs.get("logging_policy") or policies.NetworkTraceLoggingPolicy(**kwargs)
        self.http_logging_policy = kwargs.get("http_logging_policy") or policies.HttpLoggingPolicy(**kwargs)
        self.custom_hook_policy = kwargs.get("custom_hook_policy") or policies.CustomHookPolicy(**kwargs)
        self.redirect_policy = kwargs.get("redirect_policy") or policies.RedirectPolicy(**kwargs)
        self.retry_policy = kwargs.get("retry_policy") or policies.RetryPolicy(**kwargs)
        self.authentication_policy = kwargs.get("authentication_policy")
        if self.credential and not self.authentication_policy:
            self.authentication_policy = self._infer_policy(**kwargs)


class FaceSessionClientConfiguration:  # pylint: disable=too-many-instance-attributes
    """Configuration for FaceSessionClient.

    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param endpoint: Supported Cognitive Services endpoints (protocol and hostname, for example:
     https://{resource-name}.cognitiveservices.azure.com). Required.
    :type endpoint: str
    :param credential: Credential used to authenticate requests to the service. Is either a
     AzureKeyCredential type or a TokenCredential type. Required.
    :type credential: ~azure.core.credentials.AzureKeyCredential or
     ~azure.core.credentials.TokenCredential
    :keyword api_version: API Version. Known values are "v1.2-preview.1" and None. Default value is
     "v1.2-preview.1". Note that overriding this default value may result in unsupported behavior.
    :paramtype api_version: str or ~azure.ai.vision.face.models.Versions
    """

    def __init__(self, endpoint: str, credential: Union[AzureKeyCredential, "TokenCredential"], **kwargs: Any) -> None:
        api_version: str = kwargs.pop("api_version", "v1.2-preview.1")

        if endpoint is None:
            raise ValueError("Parameter 'endpoint' must not be None.")
        if credential is None:
            raise ValueError("Parameter 'credential' must not be None.")

        self.endpoint = endpoint
        self.credential = credential
        self.api_version = api_version
        self.credential_scopes = kwargs.pop("credential_scopes", ["https://cognitiveservices.azure.com/.default"])
        kwargs.setdefault("sdk_moniker", "ai-vision-face/{}".format(VERSION))
        self.polling_interval = kwargs.get("polling_interval", 30)
        self._configure(**kwargs)

    def _infer_policy(self, **kwargs):
        if isinstance(self.credential, AzureKeyCredential):
            return policies.AzureKeyCredentialPolicy(self.credential, "Ocp-Apim-Subscription-Key", **kwargs)
        if hasattr(self.credential, "get_token"):
            return policies.BearerTokenCredentialPolicy(self.credential, *self.credential_scopes, **kwargs)
        raise TypeError(f"Unsupported credential: {self.credential}")

    def _configure(self, **kwargs: Any) -> None:
        self.user_agent_policy = kwargs.get("user_agent_policy") or policies.UserAgentPolicy(**kwargs)
        self.headers_policy = kwargs.get("headers_policy") or policies.HeadersPolicy(**kwargs)
        self.proxy_policy = kwargs.get("proxy_policy") or policies.ProxyPolicy(**kwargs)
        self.logging_policy = kwargs.get("logging_policy") or policies.NetworkTraceLoggingPolicy(**kwargs)
        self.http_logging_policy = kwargs.get("http_logging_policy") or policies.HttpLoggingPolicy(**kwargs)
        self.custom_hook_policy = kwargs.get("custom_hook_policy") or policies.CustomHookPolicy(**kwargs)
        self.redirect_policy = kwargs.get("redirect_policy") or policies.RedirectPolicy(**kwargs)
        self.retry_policy = kwargs.get("retry_policy") or policies.RetryPolicy(**kwargs)
        self.authentication_policy = kwargs.get("authentication_policy")
        if self.credential and not self.authentication_policy:
            self.authentication_policy = self._infer_policy(**kwargs)
