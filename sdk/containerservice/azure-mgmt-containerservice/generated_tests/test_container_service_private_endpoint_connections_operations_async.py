# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.containerservice.aio import ContainerServiceClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer
from devtools_testutils.aio import recorded_by_proxy_async

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestContainerServicePrivateEndpointConnectionsOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(ContainerServiceClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_list(self, resource_group):
        response = await self.client.private_endpoint_connections.list(
            resource_group_name=resource_group.name,
            resource_name="str",
            api_version="2024-09-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_get(self, resource_group):
        response = await self.client.private_endpoint_connections.get(
            resource_group_name=resource_group.name,
            resource_name="str",
            private_endpoint_connection_name="str",
            api_version="2024-09-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_update(self, resource_group):
        response = await self.client.private_endpoint_connections.update(
            resource_group_name=resource_group.name,
            resource_name="str",
            private_endpoint_connection_name="str",
            parameters={
                "id": "str",
                "name": "str",
                "privateEndpoint": {"id": "str"},
                "privateLinkServiceConnectionState": {"description": "str", "status": "str"},
                "provisioningState": "str",
                "type": "str",
            },
            api_version="2024-09-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_begin_delete(self, resource_group):
        response = await (
            await self.client.private_endpoint_connections.begin_delete(
                resource_group_name=resource_group.name,
                resource_name="str",
                private_endpoint_connection_name="str",
                api_version="2024-09-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...
