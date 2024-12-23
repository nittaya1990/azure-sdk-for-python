# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.cosmosdb.aio import CosmosDBManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer
from devtools_testutils.aio import recorded_by_proxy_async

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestCosmosDBManagementCollectionPartitionOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(CosmosDBManagementClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_collection_partition_list_metrics(self, resource_group):
        response = self.client.collection_partition.list_metrics(
            resource_group_name=resource_group.name,
            account_name="str",
            database_rid="str",
            collection_rid="str",
            filter="str",
            api_version="2024-12-01-preview",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_collection_partition_list_usages(self, resource_group):
        response = self.client.collection_partition.list_usages(
            resource_group_name=resource_group.name,
            account_name="str",
            database_rid="str",
            collection_rid="str",
            api_version="2024-12-01-preview",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...
