# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, Optional
from typing_extensions import Self

from azure.core import PipelineClient
from azure.core.pipeline import policies
from azure.core.rest import HttpRequest, HttpResponse

from . import models as _models
from ._configuration import AzureDataLakeStorageRESTAPIConfiguration
from ._serialization import Deserializer, Serializer
from .operations import FileSystemOperations, PathOperations, ServiceOperations


class AzureDataLakeStorageRESTAPI:  # pylint: disable=client-accepts-api-version-keyword
    """Azure Data Lake Storage provides storage for Hadoop and other big data workloads.

    :ivar service: ServiceOperations operations
    :vartype service: azure.storage.filedatalake.operations.ServiceOperations
    :ivar file_system: FileSystemOperations operations
    :vartype file_system: azure.storage.filedatalake.operations.FileSystemOperations
    :ivar path: PathOperations operations
    :vartype path: azure.storage.filedatalake.operations.PathOperations
    :param url: The URL of the service account, container, or blob that is the target of the
     desired operation. Required.
    :type url: str
    :param base_url: Service URL. Required. Default value is "".
    :type base_url: str
    :param x_ms_lease_duration: The lease duration is required to acquire a lease, and specifies
     the duration of the lease in seconds.  The lease duration must be between 15 and 60 seconds or
     -1 for infinite lease. Default value is None.
    :type x_ms_lease_duration: int
    :keyword resource: The value must be "filesystem" for all filesystem operations. Default value
     is "filesystem". Note that overriding this default value may result in unsupported behavior.
    :paramtype resource: str
    :keyword version: Specifies the version of the operation to use for this request. Default value
     is "2025-01-05". Note that overriding this default value may result in unsupported behavior.
    :paramtype version: str
    """

    def __init__(  # pylint: disable=missing-client-constructor-parameter-credential
        self, url: str, base_url: str = "", x_ms_lease_duration: Optional[int] = None, **kwargs: Any
    ) -> None:
        self._config = AzureDataLakeStorageRESTAPIConfiguration(
            url=url, x_ms_lease_duration=x_ms_lease_duration, **kwargs
        )
        _policies = kwargs.pop("policies", None)
        if _policies is None:
            _policies = [
                policies.RequestIdPolicy(**kwargs),
                self._config.headers_policy,
                self._config.user_agent_policy,
                self._config.proxy_policy,
                policies.ContentDecodePolicy(**kwargs),
                self._config.redirect_policy,
                self._config.retry_policy,
                self._config.authentication_policy,
                self._config.custom_hook_policy,
                self._config.logging_policy,
                policies.DistributedTracingPolicy(**kwargs),
                policies.SensitiveHeaderCleanupPolicy(**kwargs) if self._config.redirect_policy else None,
                self._config.http_logging_policy,
            ]
        self._client: PipelineClient = PipelineClient(base_url=base_url, policies=_policies, **kwargs)

        client_models = {k: v for k, v in _models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.service = ServiceOperations(self._client, self._config, self._serialize, self._deserialize)
        self.file_system = FileSystemOperations(self._client, self._config, self._serialize, self._deserialize)
        self.path = PathOperations(self._client, self._config, self._serialize, self._deserialize)

    def _send_request(self, request: HttpRequest, *, stream: bool = False, **kwargs: Any) -> HttpResponse:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = client._send_request(request)
        <HttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.HttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, stream=stream, **kwargs)  # type: ignore

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> Self:
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details: Any) -> None:
        self._client.__exit__(*exc_details)
