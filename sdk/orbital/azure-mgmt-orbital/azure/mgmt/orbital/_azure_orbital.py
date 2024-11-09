# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, TYPE_CHECKING

from azure.core.rest import HttpRequest, HttpResponse
from azure.mgmt.core import ARMPipelineClient

from . import models as _models
from ._configuration import AzureOrbitalConfiguration
from ._serialization import Deserializer, Serializer
from .operations import (
    AvailableGroundStationsOperations,
    ContactProfilesOperations,
    ContactsOperations,
    Operations,
    OperationsResultsOperations,
    SpacecraftsOperations,
)

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials import TokenCredential


class AzureOrbital:  # pylint: disable=client-accepts-api-version-keyword
    """Azure Orbital service.

    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.orbital.operations.Operations
    :ivar spacecrafts: SpacecraftsOperations operations
    :vartype spacecrafts: azure.mgmt.orbital.operations.SpacecraftsOperations
    :ivar contacts: ContactsOperations operations
    :vartype contacts: azure.mgmt.orbital.operations.ContactsOperations
    :ivar contact_profiles: ContactProfilesOperations operations
    :vartype contact_profiles: azure.mgmt.orbital.operations.ContactProfilesOperations
    :ivar available_ground_stations: AvailableGroundStationsOperations operations
    :vartype available_ground_stations:
     azure.mgmt.orbital.operations.AvailableGroundStationsOperations
    :ivar operations_results: OperationsResultsOperations operations
    :vartype operations_results: azure.mgmt.orbital.operations.OperationsResultsOperations
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: The ID of the target subscription. Required.
    :type subscription_id: str
    :param base_url: Service URL. Default value is "https://management.azure.com".
    :type base_url: str
    :keyword api_version: Api Version. Default value is "2022-11-01". Note that overriding this
     default value may result in unsupported behavior.
    :paramtype api_version: str
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
     Retry-After header is present.
    """

    def __init__(
        self,
        credential: "TokenCredential",
        subscription_id: str,
        base_url: str = "https://management.azure.com",
        **kwargs: Any
    ) -> None:
        self._config = AzureOrbitalConfiguration(credential=credential, subscription_id=subscription_id, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in _models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.operations = Operations(self._client, self._config, self._serialize, self._deserialize)
        self.spacecrafts = SpacecraftsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.contacts = ContactsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.contact_profiles = ContactProfilesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.available_ground_stations = AvailableGroundStationsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.operations_results = OperationsResultsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )

    def _send_request(self, request: HttpRequest, **kwargs: Any) -> HttpResponse:
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
        return self._client.send_request(request_copy, **kwargs)

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> "AzureOrbital":
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details: Any) -> None:
        self._client.__exit__(*exc_details)
