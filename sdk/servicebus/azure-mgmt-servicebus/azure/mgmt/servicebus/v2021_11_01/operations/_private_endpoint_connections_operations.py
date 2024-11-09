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
from typing import Any, Callable, Dict, IO, Iterable, Iterator, Optional, Type, TypeVar, Union, cast, overload
import urllib.parse

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    StreamClosedError,
    StreamConsumedError,
    map_error,
)
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.polling import LROPoller, NoPolling, PollingMethod
from azure.core.rest import HttpRequest, HttpResponse
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.arm_polling import ARMPolling

from .. import models as _models
from ..._serialization import Serializer

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_list_request(
    resource_group_name: str, namespace_name: str, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2021-11-01"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/privateEndpointConnections",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", max_length=90, min_length=1
        ),
        "namespaceName": _SERIALIZER.url("namespace_name", namespace_name, "str", max_length=50, min_length=6),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_create_or_update_request(
    resource_group_name: str,
    namespace_name: str,
    private_endpoint_connection_name: str,
    subscription_id: str,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2021-11-01"))
    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/privateEndpointConnections/{privateEndpointConnectionName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", max_length=90, min_length=1
        ),
        "namespaceName": _SERIALIZER.url("namespace_name", namespace_name, "str", max_length=50, min_length=6),
        "privateEndpointConnectionName": _SERIALIZER.url(
            "private_endpoint_connection_name", private_endpoint_connection_name, "str"
        ),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, params=_params, headers=_headers, **kwargs)


def build_delete_request(
    resource_group_name: str,
    namespace_name: str,
    private_endpoint_connection_name: str,
    subscription_id: str,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2021-11-01"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/privateEndpointConnections/{privateEndpointConnectionName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", max_length=90, min_length=1
        ),
        "namespaceName": _SERIALIZER.url("namespace_name", namespace_name, "str", max_length=50, min_length=6),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "privateEndpointConnectionName": _SERIALIZER.url(
            "private_endpoint_connection_name", private_endpoint_connection_name, "str"
        ),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="DELETE", url=_url, params=_params, headers=_headers, **kwargs)


def build_get_request(
    resource_group_name: str,
    namespace_name: str,
    private_endpoint_connection_name: str,
    subscription_id: str,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2021-11-01"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/privateEndpointConnections/{privateEndpointConnectionName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", max_length=90, min_length=1
        ),
        "namespaceName": _SERIALIZER.url("namespace_name", namespace_name, "str", max_length=50, min_length=6),
        "privateEndpointConnectionName": _SERIALIZER.url(
            "private_endpoint_connection_name", private_endpoint_connection_name, "str"
        ),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


class PrivateEndpointConnectionsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.servicebus.v2021_11_01.ServiceBusManagementClient`'s
        :attr:`private_endpoint_connections` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")
        self._api_version = input_args.pop(0) if input_args else kwargs.pop("api_version")

    @distributed_trace
    def list(
        self, resource_group_name: str, namespace_name: str, **kwargs: Any
    ) -> Iterable["_models.PrivateEndpointConnection"]:
        """Gets the available PrivateEndpointConnections within a namespace.

        .. seealso::
           - https://msdn.microsoft.com/en-us/library/azure/mt639412.aspx

        :param resource_group_name: Name of the Resource group within the Azure subscription. Required.
        :type resource_group_name: str
        :param namespace_name: The namespace name. Required.
        :type namespace_name: str
        :return: An iterator like instance of either PrivateEndpointConnection or the result of
         cls(response)
        :rtype:
         ~azure.core.paging.ItemPaged[~azure.mgmt.servicebus.v2021_11_01.models.PrivateEndpointConnection]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2021-11-01"))
        cls: ClsType[_models.PrivateEndpointConnectionListResult] = kwargs.pop("cls", None)

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
                    resource_group_name=resource_group_name,
                    namespace_name=namespace_name,
                    subscription_id=self._config.subscription_id,
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
                _next_request_params["api-version"] = self._api_version
                _request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                _request.url = self._client.format_url(_request.url)
                _request.method = "GET"
            return _request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("PrivateEndpointConnectionListResult", pipeline_response)
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
    def create_or_update(
        self,
        resource_group_name: str,
        namespace_name: str,
        private_endpoint_connection_name: str,
        parameters: _models.PrivateEndpointConnection,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.PrivateEndpointConnection:
        """Creates or updates PrivateEndpointConnections of service namespace.

        .. seealso::
           - https://msdn.microsoft.com/en-us/library/azure/mt639408.aspx

        :param resource_group_name: Name of the Resource group within the Azure subscription. Required.
        :type resource_group_name: str
        :param namespace_name: The namespace name. Required.
        :type namespace_name: str
        :param private_endpoint_connection_name: The PrivateEndpointConnection name. Required.
        :type private_endpoint_connection_name: str
        :param parameters: Parameters supplied to update Status of PrivateEndPoint Connection to
         namespace resource. Required.
        :type parameters: ~azure.mgmt.servicebus.v2021_11_01.models.PrivateEndpointConnection
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: PrivateEndpointConnection or the result of cls(response)
        :rtype: ~azure.mgmt.servicebus.v2021_11_01.models.PrivateEndpointConnection
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def create_or_update(
        self,
        resource_group_name: str,
        namespace_name: str,
        private_endpoint_connection_name: str,
        parameters: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.PrivateEndpointConnection:
        """Creates or updates PrivateEndpointConnections of service namespace.

        .. seealso::
           - https://msdn.microsoft.com/en-us/library/azure/mt639408.aspx

        :param resource_group_name: Name of the Resource group within the Azure subscription. Required.
        :type resource_group_name: str
        :param namespace_name: The namespace name. Required.
        :type namespace_name: str
        :param private_endpoint_connection_name: The PrivateEndpointConnection name. Required.
        :type private_endpoint_connection_name: str
        :param parameters: Parameters supplied to update Status of PrivateEndPoint Connection to
         namespace resource. Required.
        :type parameters: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: PrivateEndpointConnection or the result of cls(response)
        :rtype: ~azure.mgmt.servicebus.v2021_11_01.models.PrivateEndpointConnection
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def create_or_update(
        self,
        resource_group_name: str,
        namespace_name: str,
        private_endpoint_connection_name: str,
        parameters: Union[_models.PrivateEndpointConnection, IO[bytes]],
        **kwargs: Any
    ) -> _models.PrivateEndpointConnection:
        """Creates or updates PrivateEndpointConnections of service namespace.

        .. seealso::
           - https://msdn.microsoft.com/en-us/library/azure/mt639408.aspx

        :param resource_group_name: Name of the Resource group within the Azure subscription. Required.
        :type resource_group_name: str
        :param namespace_name: The namespace name. Required.
        :type namespace_name: str
        :param private_endpoint_connection_name: The PrivateEndpointConnection name. Required.
        :type private_endpoint_connection_name: str
        :param parameters: Parameters supplied to update Status of PrivateEndPoint Connection to
         namespace resource. Is either a PrivateEndpointConnection type or a IO[bytes] type. Required.
        :type parameters: ~azure.mgmt.servicebus.v2021_11_01.models.PrivateEndpointConnection or
         IO[bytes]
        :return: PrivateEndpointConnection or the result of cls(response)
        :rtype: ~azure.mgmt.servicebus.v2021_11_01.models.PrivateEndpointConnection
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2021-11-01"))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.PrivateEndpointConnection] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(parameters, (IOBase, bytes)):
            _content = parameters
        else:
            _json = self._serialize.body(parameters, "PrivateEndpointConnection")

        _request = build_create_or_update_request(
            resource_group_name=resource_group_name,
            namespace_name=namespace_name,
            private_endpoint_connection_name=private_endpoint_connection_name,
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

        if response.status_code not in [200, 201, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("PrivateEndpointConnection", pipeline_response.http_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    def _delete_initial(
        self, resource_group_name: str, namespace_name: str, private_endpoint_connection_name: str, **kwargs: Any
    ) -> Iterator[bytes]:
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2021-11-01"))
        cls: ClsType[Iterator[bytes]] = kwargs.pop("cls", None)

        _request = build_delete_request(
            resource_group_name=resource_group_name,
            namespace_name=namespace_name,
            private_endpoint_connection_name=private_endpoint_connection_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _decompress = kwargs.pop("decompress", True)
        _stream = True
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 202, 204]:
            try:
                response.read()  # Load the body in memory and close the socket
            except (StreamConsumedError, StreamClosedError):
                pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = response.stream_download(self._client._pipeline, decompress=_decompress)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace
    def begin_delete(
        self, resource_group_name: str, namespace_name: str, private_endpoint_connection_name: str, **kwargs: Any
    ) -> LROPoller[None]:
        """Deletes an existing Private Endpoint Connection.

        .. seealso::
           - https://msdn.microsoft.com/en-us/library/azure/mt639389.aspx

        :param resource_group_name: Name of the Resource group within the Azure subscription. Required.
        :type resource_group_name: str
        :param namespace_name: The namespace name. Required.
        :type namespace_name: str
        :param private_endpoint_connection_name: The PrivateEndpointConnection name. Required.
        :type private_endpoint_connection_name: str
        :return: An instance of LROPoller that returns either None or the result of cls(response)
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2021-11-01"))
        cls: ClsType[None] = kwargs.pop("cls", None)
        polling: Union[bool, PollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = self._delete_initial(
                resource_group_name=resource_group_name,
                namespace_name=namespace_name,
                private_endpoint_connection_name=private_endpoint_connection_name,
                api_version=api_version,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
            raw_result.http_response.read()  # type: ignore
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):  # pylint: disable=inconsistent-return-statements
            if cls:
                return cls(pipeline_response, None, {})  # type: ignore

        if polling is True:
            polling_method: PollingMethod = cast(PollingMethod, ARMPolling(lro_delay, **kwargs))
        elif polling is False:
            polling_method = cast(PollingMethod, NoPolling())
        else:
            polling_method = polling
        if cont_token:
            return LROPoller[None].from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return LROPoller[None](self._client, raw_result, get_long_running_output, polling_method)  # type: ignore

    @distributed_trace
    def get(
        self, resource_group_name: str, namespace_name: str, private_endpoint_connection_name: str, **kwargs: Any
    ) -> _models.PrivateEndpointConnection:
        """Gets a description for the specified Private Endpoint Connection.

        .. seealso::
           - https://msdn.microsoft.com/en-us/library/azure/mt639379.aspx

        :param resource_group_name: Name of the Resource group within the Azure subscription. Required.
        :type resource_group_name: str
        :param namespace_name: The namespace name. Required.
        :type namespace_name: str
        :param private_endpoint_connection_name: The PrivateEndpointConnection name. Required.
        :type private_endpoint_connection_name: str
        :return: PrivateEndpointConnection or the result of cls(response)
        :rtype: ~azure.mgmt.servicebus.v2021_11_01.models.PrivateEndpointConnection
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2021-11-01"))
        cls: ClsType[_models.PrivateEndpointConnection] = kwargs.pop("cls", None)

        _request = build_get_request(
            resource_group_name=resource_group_name,
            namespace_name=namespace_name,
            private_endpoint_connection_name=private_endpoint_connection_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
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

        deserialized = self._deserialize("PrivateEndpointConnection", pipeline_response.http_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore
