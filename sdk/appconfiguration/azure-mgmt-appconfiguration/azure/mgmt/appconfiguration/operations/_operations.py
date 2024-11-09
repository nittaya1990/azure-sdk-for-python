# pylint: disable=too-many-lines,too-many-statements
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
import sys
from typing import Any, Callable, Dict, IO, Iterable, Optional, Type, TypeVar, Union, overload
import urllib.parse

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.rest import HttpRequest, HttpResponse
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models as _models
from .._serialization import Serializer

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_check_name_availability_request(subscription_id: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2024-05-01"))
    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url", "/subscriptions/{subscriptionId}/providers/Microsoft.AppConfiguration/checkNameAvailability"
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


def build_list_request(*, skip_token: Optional[str] = None, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2024-05-01"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/providers/Microsoft.AppConfiguration/operations")

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")
    if skip_token is not None:
        _params["$skipToken"] = _SERIALIZER.query("skip_token", skip_token, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_regional_check_name_availability_request(  # pylint: disable=name-too-long
    location: str, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2024-05-01"))
    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/providers/Microsoft.AppConfiguration/locations/{location}/checkNameAvailability",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "location": _SERIALIZER.url("location", location, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


class Operations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.appconfiguration.AppConfigurationManagementClient`'s
        :attr:`operations` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @overload
    def check_name_availability(
        self,
        check_name_availability_parameters: _models.CheckNameAvailabilityParameters,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.NameAvailabilityStatus:
        """Checks whether the configuration store name is available for use.

        :param check_name_availability_parameters: The object containing information for the
         availability request. Required.
        :type check_name_availability_parameters:
         ~azure.mgmt.appconfiguration.models.CheckNameAvailabilityParameters
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: NameAvailabilityStatus or the result of cls(response)
        :rtype: ~azure.mgmt.appconfiguration.models.NameAvailabilityStatus
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def check_name_availability(
        self, check_name_availability_parameters: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.NameAvailabilityStatus:
        """Checks whether the configuration store name is available for use.

        :param check_name_availability_parameters: The object containing information for the
         availability request. Required.
        :type check_name_availability_parameters: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: NameAvailabilityStatus or the result of cls(response)
        :rtype: ~azure.mgmt.appconfiguration.models.NameAvailabilityStatus
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def check_name_availability(
        self,
        check_name_availability_parameters: Union[_models.CheckNameAvailabilityParameters, IO[bytes]],
        **kwargs: Any
    ) -> _models.NameAvailabilityStatus:
        """Checks whether the configuration store name is available for use.

        :param check_name_availability_parameters: The object containing information for the
         availability request. Is either a CheckNameAvailabilityParameters type or a IO[bytes] type.
         Required.
        :type check_name_availability_parameters:
         ~azure.mgmt.appconfiguration.models.CheckNameAvailabilityParameters or IO[bytes]
        :return: NameAvailabilityStatus or the result of cls(response)
        :rtype: ~azure.mgmt.appconfiguration.models.NameAvailabilityStatus
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.NameAvailabilityStatus] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(check_name_availability_parameters, (IOBase, bytes)):
            _content = check_name_availability_parameters
        else:
            _json = self._serialize.body(check_name_availability_parameters, "CheckNameAvailabilityParameters")

        _request = build_check_name_availability_request(
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("NameAvailabilityStatus", pipeline_response.http_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace
    def list(self, skip_token: Optional[str] = None, **kwargs: Any) -> Iterable["_models.OperationDefinition"]:
        """Lists the operations available from this provider.

        :param skip_token: A skip token is used to continue retrieving items after an operation returns
         a partial result. If a previous response contains a nextLink element, the value of the nextLink
         element will include a skipToken parameter that specifies a starting point to use for
         subsequent calls. Default value is None.
        :type skip_token: str
        :return: An iterator like instance of either OperationDefinition or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.mgmt.appconfiguration.models.OperationDefinition]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[_models.OperationDefinitionListResult] = kwargs.pop("cls", None)

        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                _request = build_list_request(
                    skip_token=skip_token,
                    api_version=api_version,
                    headers=_headers,
                    params=_params,
                )
                _request.url = self._client.format_url(_request.url)

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                _request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                _request.url = self._client.format_url(_request.url)
                _request.method = "GET"
            return _request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("OperationDefinitionListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            _request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
                _request, stream=_stream, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    @overload
    def regional_check_name_availability(
        self,
        location: str,
        check_name_availability_parameters: _models.CheckNameAvailabilityParameters,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.NameAvailabilityStatus:
        """Checks whether the configuration store name is available for use.

        :param location: The location in which uniqueness will be verified. Required.
        :type location: str
        :param check_name_availability_parameters: The object containing information for the
         availability request. Required.
        :type check_name_availability_parameters:
         ~azure.mgmt.appconfiguration.models.CheckNameAvailabilityParameters
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: NameAvailabilityStatus or the result of cls(response)
        :rtype: ~azure.mgmt.appconfiguration.models.NameAvailabilityStatus
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def regional_check_name_availability(
        self,
        location: str,
        check_name_availability_parameters: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.NameAvailabilityStatus:
        """Checks whether the configuration store name is available for use.

        :param location: The location in which uniqueness will be verified. Required.
        :type location: str
        :param check_name_availability_parameters: The object containing information for the
         availability request. Required.
        :type check_name_availability_parameters: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: NameAvailabilityStatus or the result of cls(response)
        :rtype: ~azure.mgmt.appconfiguration.models.NameAvailabilityStatus
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def regional_check_name_availability(
        self,
        location: str,
        check_name_availability_parameters: Union[_models.CheckNameAvailabilityParameters, IO[bytes]],
        **kwargs: Any
    ) -> _models.NameAvailabilityStatus:
        """Checks whether the configuration store name is available for use.

        :param location: The location in which uniqueness will be verified. Required.
        :type location: str
        :param check_name_availability_parameters: The object containing information for the
         availability request. Is either a CheckNameAvailabilityParameters type or a IO[bytes] type.
         Required.
        :type check_name_availability_parameters:
         ~azure.mgmt.appconfiguration.models.CheckNameAvailabilityParameters or IO[bytes]
        :return: NameAvailabilityStatus or the result of cls(response)
        :rtype: ~azure.mgmt.appconfiguration.models.NameAvailabilityStatus
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.NameAvailabilityStatus] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(check_name_availability_parameters, (IOBase, bytes)):
            _content = check_name_availability_parameters
        else:
            _json = self._serialize.body(check_name_availability_parameters, "CheckNameAvailabilityParameters")

        _request = build_regional_check_name_availability_request(
            location=location,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("NameAvailabilityStatus", pipeline_response.http_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore
