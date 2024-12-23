# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, AsyncIterable, Callable, Dict, Optional, TypeVar
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
from azure.core.rest import AsyncHttpResponse, HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ...operations._restorable_mongodb_resources_operations import build_list_request

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class RestorableMongodbResourcesOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.cosmosdb.aio.CosmosDBManagementClient`'s
        :attr:`restorable_mongodb_resources` attribute.
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
        location: str,
        instance_id: str,
        restore_location: Optional[str] = None,
        restore_timestamp_in_utc: Optional[str] = None,
        **kwargs: Any
    ) -> AsyncIterable["_models.RestorableMongodbResourcesGetResult"]:
        """Return a list of database and collection combo that exist on the account at the given timestamp
        and location. This helps in scenarios to validate what resources exist at given timestamp and
        location. This API requires
        'Microsoft.DocumentDB/locations/restorableDatabaseAccounts/.../read' permission.

        :param location: Cosmos DB region, with spaces between words and each word capitalized.
         Required.
        :type location: str
        :param instance_id: The instanceId GUID of a restorable database account. Required.
        :type instance_id: str
        :param restore_location: The location where the restorable resources are located. Default value
         is None.
        :type restore_location: str
        :param restore_timestamp_in_utc: The timestamp when the restorable resources existed. Default
         value is None.
        :type restore_timestamp_in_utc: str
        :return: An iterator like instance of either RestorableMongodbResourcesGetResult or the result
         of cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.cosmosdb.models.RestorableMongodbResourcesGetResult]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[_models.RestorableMongodbResourcesListResult] = kwargs.pop("cls", None)

        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                _request = build_list_request(
                    location=location,
                    instance_id=instance_id,
                    subscription_id=self._config.subscription_id,
                    restore_location=restore_location,
                    restore_timestamp_in_utc=restore_timestamp_in_utc,
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

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("RestorableMongodbResourcesListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            _request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
                _request, stream=_stream, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)
