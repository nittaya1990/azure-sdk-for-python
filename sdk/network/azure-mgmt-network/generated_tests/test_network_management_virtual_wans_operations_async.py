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
class TestNetworkManagementVirtualWansOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(NetworkManagementClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_get(self, resource_group):
        response = await self.client.virtual_wans.get(
            resource_group_name=resource_group.name,
            virtual_wan_name="str",
            api_version="2024-03-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_begin_create_or_update(self, resource_group):
        response = await (
            await self.client.virtual_wans.begin_create_or_update(
                resource_group_name=resource_group.name,
                virtual_wan_name="str",
                wan_parameters={
                    "allowBranchToBranchTraffic": bool,
                    "allowVnetToVnetTraffic": bool,
                    "disableVpnEncryption": bool,
                    "etag": "str",
                    "id": "str",
                    "location": "str",
                    "name": "str",
                    "office365LocalBreakoutCategory": "str",
                    "provisioningState": "str",
                    "tags": {"str": "str"},
                    "type": "str",
                    "virtualHubs": [{"id": "str"}],
                    "vpnSites": [{"id": "str"}],
                },
                api_version="2024-03-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_update_tags(self, resource_group):
        response = await self.client.virtual_wans.update_tags(
            resource_group_name=resource_group.name,
            virtual_wan_name="str",
            wan_parameters={"tags": {"str": "str"}},
            api_version="2024-03-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_begin_delete(self, resource_group):
        response = await (
            await self.client.virtual_wans.begin_delete(
                resource_group_name=resource_group.name,
                virtual_wan_name="str",
                api_version="2024-03-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_list_by_resource_group(self, resource_group):
        response = self.client.virtual_wans.list_by_resource_group(
            resource_group_name=resource_group.name,
            api_version="2024-03-01",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_list(self, resource_group):
        response = self.client.virtual_wans.list(
            api_version="2024-03-01",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...
