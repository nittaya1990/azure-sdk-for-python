# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.network.aio import NetworkManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer
from devtools_testutils.aio import recorded_by_proxy_async

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestNetworkManagementNetworkVirtualAppliancesOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(NetworkManagementClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_begin_delete(self, resource_group):
        response = await (
            await self.client.network_virtual_appliances.begin_delete(
                resource_group_name=resource_group.name,
                network_virtual_appliance_name="str",
                api_version="2024-03-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_get(self, resource_group):
        response = await self.client.network_virtual_appliances.get(
            resource_group_name=resource_group.name,
            network_virtual_appliance_name="str",
            api_version="2024-03-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_update_tags(self, resource_group):
        response = await self.client.network_virtual_appliances.update_tags(
            resource_group_name=resource_group.name,
            network_virtual_appliance_name="str",
            parameters={"tags": {"str": "str"}},
            api_version="2024-03-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_begin_create_or_update(self, resource_group):
        response = await (
            await self.client.network_virtual_appliances.begin_create_or_update(
                resource_group_name=resource_group.name,
                network_virtual_appliance_name="str",
                parameters={
                    "additionalNics": [{"hasPublicIp": bool, "name": "str"}],
                    "addressPrefix": "str",
                    "bootStrapConfigurationBlobs": ["str"],
                    "cloudInitConfiguration": "str",
                    "cloudInitConfigurationBlobs": ["str"],
                    "delegation": {"provisioningState": "str", "serviceName": "str"},
                    "deploymentType": "str",
                    "etag": "str",
                    "id": "str",
                    "identity": {
                        "principalId": "str",
                        "tenantId": "str",
                        "type": "str",
                        "userAssignedIdentities": {"str": {"clientId": "str", "principalId": "str"}},
                    },
                    "inboundSecurityRules": [{"id": "str"}],
                    "internetIngressPublicIps": [{"id": "str"}],
                    "location": "str",
                    "name": "str",
                    "networkProfile": {
                        "networkInterfaceConfigurations": [
                            {
                                "properties": {"ipConfigurations": [{"name": "str", "properties": {"primary": bool}}]},
                                "type": "str",
                            }
                        ]
                    },
                    "nvaSku": {"bundledScaleUnit": "str", "marketPlaceVersion": "str", "vendor": "str"},
                    "partnerManagedResource": {
                        "id": "str",
                        "internalLoadBalancerId": "str",
                        "standardLoadBalancerId": "str",
                    },
                    "provisioningState": "str",
                    "sshPublicKey": "str",
                    "tags": {"str": "str"},
                    "type": "str",
                    "virtualApplianceAsn": 0,
                    "virtualApplianceConnections": [{"id": "str"}],
                    "virtualApplianceNics": [
                        {
                            "instanceName": "str",
                            "name": "str",
                            "nicType": "str",
                            "privateIpAddress": "str",
                            "publicIpAddress": "str",
                        }
                    ],
                    "virtualApplianceSites": [{"id": "str"}],
                    "virtualHub": {"id": "str"},
                },
                api_version="2024-03-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_begin_restart(self, resource_group):
        response = await (
            await self.client.network_virtual_appliances.begin_restart(
                resource_group_name=resource_group.name,
                network_virtual_appliance_name="str",
                api_version="2024-03-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_list_by_resource_group(self, resource_group):
        response = self.client.network_virtual_appliances.list_by_resource_group(
            resource_group_name=resource_group.name,
            api_version="2024-03-01",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_list(self, resource_group):
        response = self.client.network_virtual_appliances.list(
            api_version="2024-03-01",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...
