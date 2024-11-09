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
from typing import Any, AsyncIterable, Callable, Dict, IO, Optional, Type, TypeVar, Union, overload
import urllib.parse

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._webhook_operations import (
    build_create_or_update_request,
    build_delete_request,
    build_get_request,
    build_list_request,
    build_update_request,
)

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class WebhookOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.appcomplianceautomation.aio.AppComplianceAutomationMgmtClient`'s
        :attr:`webhook` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def list(
        self,
        report_name: str,
        skip_token: Optional[str] = None,
        top: Optional[int] = None,
        select: Optional[str] = None,
        filter: Optional[str] = None,
        orderby: Optional[str] = None,
        offer_guid: Optional[str] = None,
        report_creator_tenant_id: Optional[str] = None,
        **kwargs: Any
    ) -> AsyncIterable["_models.WebhookResource"]:
        """Get the AppComplianceAutomation webhook list.

        :param report_name: Report Name. Required.
        :type report_name: str
        :param skip_token: Skip over when retrieving results. Default value is None.
        :type skip_token: str
        :param top: Number of elements to return when retrieving results. Default value is None.
        :type top: int
        :param select: OData Select statement. Limits the properties on each entry to just those
         requested, e.g. ?$select=reportName,id. Default value is None.
        :type select: str
        :param filter: The filter to apply on the operation. Default value is None.
        :type filter: str
        :param orderby: OData order by query option. Default value is None.
        :type orderby: str
        :param offer_guid: The offerGuid which mapping to the reports. Default value is None.
        :type offer_guid: str
        :param report_creator_tenant_id: The tenant id of the report creator. Default value is None.
        :type report_creator_tenant_id: str
        :return: An iterator like instance of either WebhookResource or the result of cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.appcomplianceautomation.models.WebhookResource]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[_models.WebhookResourceListResult] = kwargs.pop("cls", None)

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
                    report_name=report_name,
                    skip_token=skip_token,
                    top=top,
                    select=select,
                    filter=filter,
                    orderby=orderby,
                    offer_guid=offer_guid,
                    report_creator_tenant_id=report_creator_tenant_id,
                    api_version=api_version,
                    headers=_headers,
                    params=_params,
                )
                _request = _convert_request(_request)
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
                _request = _convert_request(_request)
                _request.url = self._client.format_url(_request.url)
                _request.method = "GET"
            return _request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("WebhookResourceListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            _request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
                _request, stream=_stream, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    @distributed_trace_async
    async def get(self, report_name: str, webhook_name: str, **kwargs: Any) -> _models.WebhookResource:
        """Get the AppComplianceAutomation webhook and its properties.

        :param report_name: Report Name. Required.
        :type report_name: str
        :param webhook_name: Webhook Name. Required.
        :type webhook_name: str
        :return: WebhookResource or the result of cls(response)
        :rtype: ~azure.mgmt.appcomplianceautomation.models.WebhookResource
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[_models.WebhookResource] = kwargs.pop("cls", None)

        _request = build_get_request(
            report_name=report_name,
            webhook_name=webhook_name,
            api_version=api_version,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("WebhookResource", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def create_or_update(
        self,
        report_name: str,
        webhook_name: str,
        properties: _models.WebhookResource,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.WebhookResource:
        """Create a new AppComplianceAutomation webhook or update an exiting AppComplianceAutomation
        webhook.

        :param report_name: Report Name. Required.
        :type report_name: str
        :param webhook_name: Webhook Name. Required.
        :type webhook_name: str
        :param properties: Parameters for the create or update operation. Required.
        :type properties: ~azure.mgmt.appcomplianceautomation.models.WebhookResource
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: WebhookResource or the result of cls(response)
        :rtype: ~azure.mgmt.appcomplianceautomation.models.WebhookResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def create_or_update(
        self,
        report_name: str,
        webhook_name: str,
        properties: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.WebhookResource:
        """Create a new AppComplianceAutomation webhook or update an exiting AppComplianceAutomation
        webhook.

        :param report_name: Report Name. Required.
        :type report_name: str
        :param webhook_name: Webhook Name. Required.
        :type webhook_name: str
        :param properties: Parameters for the create or update operation. Required.
        :type properties: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: WebhookResource or the result of cls(response)
        :rtype: ~azure.mgmt.appcomplianceautomation.models.WebhookResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def create_or_update(
        self, report_name: str, webhook_name: str, properties: Union[_models.WebhookResource, IO[bytes]], **kwargs: Any
    ) -> _models.WebhookResource:
        """Create a new AppComplianceAutomation webhook or update an exiting AppComplianceAutomation
        webhook.

        :param report_name: Report Name. Required.
        :type report_name: str
        :param webhook_name: Webhook Name. Required.
        :type webhook_name: str
        :param properties: Parameters for the create or update operation. Is either a WebhookResource
         type or a IO[bytes] type. Required.
        :type properties: ~azure.mgmt.appcomplianceautomation.models.WebhookResource or IO[bytes]
        :return: WebhookResource or the result of cls(response)
        :rtype: ~azure.mgmt.appcomplianceautomation.models.WebhookResource
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
        cls: ClsType[_models.WebhookResource] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(properties, (IOBase, bytes)):
            _content = properties
        else:
            _json = self._serialize.body(properties, "WebhookResource")

        _request = build_create_or_update_request(
            report_name=report_name,
            webhook_name=webhook_name,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize("WebhookResource", pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize("WebhookResource", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def update(
        self,
        report_name: str,
        webhook_name: str,
        properties: _models.WebhookResourcePatch,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.WebhookResource:
        """Update an exiting AppComplianceAutomation webhook.

        :param report_name: Report Name. Required.
        :type report_name: str
        :param webhook_name: Webhook Name. Required.
        :type webhook_name: str
        :param properties: Parameters for the create or update operation. Required.
        :type properties: ~azure.mgmt.appcomplianceautomation.models.WebhookResourcePatch
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: WebhookResource or the result of cls(response)
        :rtype: ~azure.mgmt.appcomplianceautomation.models.WebhookResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def update(
        self,
        report_name: str,
        webhook_name: str,
        properties: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.WebhookResource:
        """Update an exiting AppComplianceAutomation webhook.

        :param report_name: Report Name. Required.
        :type report_name: str
        :param webhook_name: Webhook Name. Required.
        :type webhook_name: str
        :param properties: Parameters for the create or update operation. Required.
        :type properties: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: WebhookResource or the result of cls(response)
        :rtype: ~azure.mgmt.appcomplianceautomation.models.WebhookResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def update(
        self,
        report_name: str,
        webhook_name: str,
        properties: Union[_models.WebhookResourcePatch, IO[bytes]],
        **kwargs: Any
    ) -> _models.WebhookResource:
        """Update an exiting AppComplianceAutomation webhook.

        :param report_name: Report Name. Required.
        :type report_name: str
        :param webhook_name: Webhook Name. Required.
        :type webhook_name: str
        :param properties: Parameters for the create or update operation. Is either a
         WebhookResourcePatch type or a IO[bytes] type. Required.
        :type properties: ~azure.mgmt.appcomplianceautomation.models.WebhookResourcePatch or IO[bytes]
        :return: WebhookResource or the result of cls(response)
        :rtype: ~azure.mgmt.appcomplianceautomation.models.WebhookResource
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
        cls: ClsType[_models.WebhookResource] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(properties, (IOBase, bytes)):
            _content = properties
        else:
            _json = self._serialize.body(properties, "WebhookResourcePatch")

        _request = build_update_request(
            report_name=report_name,
            webhook_name=webhook_name,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("WebhookResource", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace_async
    async def delete(  # pylint: disable=inconsistent-return-statements
        self, report_name: str, webhook_name: str, **kwargs: Any
    ) -> None:
        """Delete an AppComplianceAutomation webhook.

        :param report_name: Report Name. Required.
        :type report_name: str
        :param webhook_name: Webhook Name. Required.
        :type webhook_name: str
        :return: None or the result of cls(response)
        :rtype: None
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_delete_request(
            report_name=report_name,
            webhook_name=webhook_name,
            api_version=api_version,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore
