# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, Awaitable, TYPE_CHECKING

from azure.core.rest import AsyncHttpResponse, HttpRequest
from azure.mgmt.core import AsyncARMPipelineClient

from .. import models as _models
from .._serialization import Deserializer, Serializer
from ._configuration import SiteRecoveryManagementClientConfiguration
from .operations import (
    MigrationRecoveryPointsOperations,
    Operations,
    RecoveryPointsOperations,
    ReplicationAlertSettingsOperations,
    ReplicationAppliancesOperations,
    ReplicationEligibilityResultsOperations,
    ReplicationEventsOperations,
    ReplicationFabricsOperations,
    ReplicationJobsOperations,
    ReplicationLogicalNetworksOperations,
    ReplicationMigrationItemsOperations,
    ReplicationNetworkMappingsOperations,
    ReplicationNetworksOperations,
    ReplicationPoliciesOperations,
    ReplicationProtectableItemsOperations,
    ReplicationProtectedItemsOperations,
    ReplicationProtectionContainerMappingsOperations,
    ReplicationProtectionContainersOperations,
    ReplicationProtectionIntentsOperations,
    ReplicationRecoveryPlansOperations,
    ReplicationRecoveryServicesProvidersOperations,
    ReplicationStorageClassificationMappingsOperations,
    ReplicationStorageClassificationsOperations,
    ReplicationVaultHealthOperations,
    ReplicationVaultSettingOperations,
    ReplicationvCentersOperations,
    SupportedOperatingSystemsOperations,
    TargetComputeSizesOperations,
)

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential


class SiteRecoveryManagementClient:  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """SiteRecoveryManagementClient.

    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.recoveryservicessiterecovery.aio.operations.Operations
    :ivar replication_alert_settings: ReplicationAlertSettingsOperations operations
    :vartype replication_alert_settings:
     azure.mgmt.recoveryservicessiterecovery.aio.operations.ReplicationAlertSettingsOperations
    :ivar replication_appliances: ReplicationAppliancesOperations operations
    :vartype replication_appliances:
     azure.mgmt.recoveryservicessiterecovery.aio.operations.ReplicationAppliancesOperations
    :ivar replication_eligibility_results: ReplicationEligibilityResultsOperations operations
    :vartype replication_eligibility_results:
     azure.mgmt.recoveryservicessiterecovery.aio.operations.ReplicationEligibilityResultsOperations
    :ivar replication_events: ReplicationEventsOperations operations
    :vartype replication_events:
     azure.mgmt.recoveryservicessiterecovery.aio.operations.ReplicationEventsOperations
    :ivar replication_fabrics: ReplicationFabricsOperations operations
    :vartype replication_fabrics:
     azure.mgmt.recoveryservicessiterecovery.aio.operations.ReplicationFabricsOperations
    :ivar replication_logical_networks: ReplicationLogicalNetworksOperations operations
    :vartype replication_logical_networks:
     azure.mgmt.recoveryservicessiterecovery.aio.operations.ReplicationLogicalNetworksOperations
    :ivar replication_networks: ReplicationNetworksOperations operations
    :vartype replication_networks:
     azure.mgmt.recoveryservicessiterecovery.aio.operations.ReplicationNetworksOperations
    :ivar replication_network_mappings: ReplicationNetworkMappingsOperations operations
    :vartype replication_network_mappings:
     azure.mgmt.recoveryservicessiterecovery.aio.operations.ReplicationNetworkMappingsOperations
    :ivar replication_protection_containers: ReplicationProtectionContainersOperations operations
    :vartype replication_protection_containers:
     azure.mgmt.recoveryservicessiterecovery.aio.operations.ReplicationProtectionContainersOperations
    :ivar replication_migration_items: ReplicationMigrationItemsOperations operations
    :vartype replication_migration_items:
     azure.mgmt.recoveryservicessiterecovery.aio.operations.ReplicationMigrationItemsOperations
    :ivar migration_recovery_points: MigrationRecoveryPointsOperations operations
    :vartype migration_recovery_points:
     azure.mgmt.recoveryservicessiterecovery.aio.operations.MigrationRecoveryPointsOperations
    :ivar replication_protectable_items: ReplicationProtectableItemsOperations operations
    :vartype replication_protectable_items:
     azure.mgmt.recoveryservicessiterecovery.aio.operations.ReplicationProtectableItemsOperations
    :ivar replication_protected_items: ReplicationProtectedItemsOperations operations
    :vartype replication_protected_items:
     azure.mgmt.recoveryservicessiterecovery.aio.operations.ReplicationProtectedItemsOperations
    :ivar recovery_points: RecoveryPointsOperations operations
    :vartype recovery_points:
     azure.mgmt.recoveryservicessiterecovery.aio.operations.RecoveryPointsOperations
    :ivar target_compute_sizes: TargetComputeSizesOperations operations
    :vartype target_compute_sizes:
     azure.mgmt.recoveryservicessiterecovery.aio.operations.TargetComputeSizesOperations
    :ivar replication_protection_container_mappings:
     ReplicationProtectionContainerMappingsOperations operations
    :vartype replication_protection_container_mappings:
     azure.mgmt.recoveryservicessiterecovery.aio.operations.ReplicationProtectionContainerMappingsOperations
    :ivar replication_recovery_services_providers: ReplicationRecoveryServicesProvidersOperations
     operations
    :vartype replication_recovery_services_providers:
     azure.mgmt.recoveryservicessiterecovery.aio.operations.ReplicationRecoveryServicesProvidersOperations
    :ivar replication_storage_classifications: ReplicationStorageClassificationsOperations
     operations
    :vartype replication_storage_classifications:
     azure.mgmt.recoveryservicessiterecovery.aio.operations.ReplicationStorageClassificationsOperations
    :ivar replication_storage_classification_mappings:
     ReplicationStorageClassificationMappingsOperations operations
    :vartype replication_storage_classification_mappings:
     azure.mgmt.recoveryservicessiterecovery.aio.operations.ReplicationStorageClassificationMappingsOperations
    :ivar replicationv_centers: ReplicationvCentersOperations operations
    :vartype replicationv_centers:
     azure.mgmt.recoveryservicessiterecovery.aio.operations.ReplicationvCentersOperations
    :ivar replication_jobs: ReplicationJobsOperations operations
    :vartype replication_jobs:
     azure.mgmt.recoveryservicessiterecovery.aio.operations.ReplicationJobsOperations
    :ivar replication_policies: ReplicationPoliciesOperations operations
    :vartype replication_policies:
     azure.mgmt.recoveryservicessiterecovery.aio.operations.ReplicationPoliciesOperations
    :ivar replication_protection_intents: ReplicationProtectionIntentsOperations operations
    :vartype replication_protection_intents:
     azure.mgmt.recoveryservicessiterecovery.aio.operations.ReplicationProtectionIntentsOperations
    :ivar replication_recovery_plans: ReplicationRecoveryPlansOperations operations
    :vartype replication_recovery_plans:
     azure.mgmt.recoveryservicessiterecovery.aio.operations.ReplicationRecoveryPlansOperations
    :ivar supported_operating_systems: SupportedOperatingSystemsOperations operations
    :vartype supported_operating_systems:
     azure.mgmt.recoveryservicessiterecovery.aio.operations.SupportedOperatingSystemsOperations
    :ivar replication_vault_health: ReplicationVaultHealthOperations operations
    :vartype replication_vault_health:
     azure.mgmt.recoveryservicessiterecovery.aio.operations.ReplicationVaultHealthOperations
    :ivar replication_vault_setting: ReplicationVaultSettingOperations operations
    :vartype replication_vault_setting:
     azure.mgmt.recoveryservicessiterecovery.aio.operations.ReplicationVaultSettingOperations
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: The subscription Id. Required.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group where the recovery services vault is
     present. Required.
    :type resource_group_name: str
    :param resource_name: The name of the recovery services vault. Required.
    :type resource_name: str
    :param base_url: Service URL. Default value is "https://management.azure.com".
    :type base_url: str
    :keyword api_version: Api Version. Default value is "2023-08-01". Note that overriding this
     default value may result in unsupported behavior.
    :paramtype api_version: str
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
     Retry-After header is present.
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        subscription_id: str,
        resource_group_name: str,
        resource_name: str,
        base_url: str = "https://management.azure.com",
        **kwargs: Any
    ) -> None:
        self._config = SiteRecoveryManagementClientConfiguration(
            credential=credential,
            subscription_id=subscription_id,
            resource_group_name=resource_group_name,
            resource_name=resource_name,
            **kwargs
        )
        self._client: AsyncARMPipelineClient = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in _models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.operations = Operations(self._client, self._config, self._serialize, self._deserialize)
        self.replication_alert_settings = ReplicationAlertSettingsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.replication_appliances = ReplicationAppliancesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.replication_eligibility_results = ReplicationEligibilityResultsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.replication_events = ReplicationEventsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.replication_fabrics = ReplicationFabricsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.replication_logical_networks = ReplicationLogicalNetworksOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.replication_networks = ReplicationNetworksOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.replication_network_mappings = ReplicationNetworkMappingsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.replication_protection_containers = ReplicationProtectionContainersOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.replication_migration_items = ReplicationMigrationItemsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.migration_recovery_points = MigrationRecoveryPointsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.replication_protectable_items = ReplicationProtectableItemsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.replication_protected_items = ReplicationProtectedItemsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.recovery_points = RecoveryPointsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.target_compute_sizes = TargetComputeSizesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.replication_protection_container_mappings = ReplicationProtectionContainerMappingsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.replication_recovery_services_providers = ReplicationRecoveryServicesProvidersOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.replication_storage_classifications = ReplicationStorageClassificationsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.replication_storage_classification_mappings = ReplicationStorageClassificationMappingsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.replicationv_centers = ReplicationvCentersOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.replication_jobs = ReplicationJobsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.replication_policies = ReplicationPoliciesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.replication_protection_intents = ReplicationProtectionIntentsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.replication_recovery_plans = ReplicationRecoveryPlansOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.supported_operating_systems = SupportedOperatingSystemsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.replication_vault_health = ReplicationVaultHealthOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.replication_vault_setting = ReplicationVaultSettingOperations(
            self._client, self._config, self._serialize, self._deserialize
        )

    def _send_request(self, request: HttpRequest, **kwargs: Any) -> Awaitable[AsyncHttpResponse]:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = await client._send_request(request)
        <AsyncHttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.AsyncHttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, **kwargs)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "SiteRecoveryManagementClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details: Any) -> None:
        await self._client.__aexit__(*exc_details)
