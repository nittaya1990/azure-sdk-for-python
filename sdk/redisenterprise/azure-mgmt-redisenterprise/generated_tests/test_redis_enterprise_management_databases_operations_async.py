# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.redisenterprise.aio import RedisEnterpriseManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer
from devtools_testutils.aio import recorded_by_proxy_async

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestRedisEnterpriseManagementDatabasesOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(RedisEnterpriseManagementClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_list_by_cluster(self, resource_group):
        response = self.client.databases.list_by_cluster(
            resource_group_name=resource_group.name,
            cluster_name="str",
            api_version="2024-09-01-preview",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_begin_create(self, resource_group):
        response = await (
            await self.client.databases.begin_create(
                resource_group_name=resource_group.name,
                cluster_name="str",
                database_name="str",
                parameters={
                    "accessKeysAuthentication": "str",
                    "clientProtocol": "str",
                    "clusteringPolicy": "str",
                    "deferUpgrade": "str",
                    "evictionPolicy": "str",
                    "geoReplication": {"groupNickname": "str", "linkedDatabases": [{"id": "str", "state": "str"}]},
                    "id": "str",
                    "modules": [{"name": "str", "args": "str", "version": "str"}],
                    "name": "str",
                    "persistence": {
                        "aofEnabled": bool,
                        "aofFrequency": "str",
                        "rdbEnabled": bool,
                        "rdbFrequency": "str",
                    },
                    "port": 0,
                    "provisioningState": "str",
                    "redisVersion": "str",
                    "resourceState": "str",
                    "systemData": {
                        "createdAt": "2020-02-20 00:00:00",
                        "createdBy": "str",
                        "createdByType": "str",
                        "lastModifiedAt": "2020-02-20 00:00:00",
                        "lastModifiedBy": "str",
                        "lastModifiedByType": "str",
                    },
                    "type": "str",
                },
                api_version="2024-09-01-preview",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_begin_update(self, resource_group):
        response = await (
            await self.client.databases.begin_update(
                resource_group_name=resource_group.name,
                cluster_name="str",
                database_name="str",
                parameters={
                    "accessKeysAuthentication": "str",
                    "clientProtocol": "str",
                    "clusteringPolicy": "str",
                    "deferUpgrade": "str",
                    "evictionPolicy": "str",
                    "geoReplication": {"groupNickname": "str", "linkedDatabases": [{"id": "str", "state": "str"}]},
                    "modules": [{"name": "str", "args": "str", "version": "str"}],
                    "persistence": {
                        "aofEnabled": bool,
                        "aofFrequency": "str",
                        "rdbEnabled": bool,
                        "rdbFrequency": "str",
                    },
                    "port": 0,
                    "provisioningState": "str",
                    "redisVersion": "str",
                    "resourceState": "str",
                },
                api_version="2024-09-01-preview",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_get(self, resource_group):
        response = await self.client.databases.get(
            resource_group_name=resource_group.name,
            cluster_name="str",
            database_name="str",
            api_version="2024-09-01-preview",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_begin_delete(self, resource_group):
        response = await (
            await self.client.databases.begin_delete(
                resource_group_name=resource_group.name,
                cluster_name="str",
                database_name="str",
                api_version="2024-09-01-preview",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_list_keys(self, resource_group):
        response = await self.client.databases.list_keys(
            resource_group_name=resource_group.name,
            cluster_name="str",
            database_name="str",
            api_version="2024-09-01-preview",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_begin_regenerate_key(self, resource_group):
        response = await (
            await self.client.databases.begin_regenerate_key(
                resource_group_name=resource_group.name,
                cluster_name="str",
                database_name="str",
                parameters={"keyType": "str"},
                api_version="2024-09-01-preview",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_begin_import_method(self, resource_group):
        response = await (
            await self.client.databases.begin_import_method(
                resource_group_name=resource_group.name,
                cluster_name="str",
                database_name="str",
                parameters={"sasUris": ["str"]},
                api_version="2024-09-01-preview",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_begin_export(self, resource_group):
        response = await (
            await self.client.databases.begin_export(
                resource_group_name=resource_group.name,
                cluster_name="str",
                database_name="str",
                parameters={"sasUri": "str"},
                api_version="2024-09-01-preview",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_begin_force_unlink(self, resource_group):
        response = await (
            await self.client.databases.begin_force_unlink(
                resource_group_name=resource_group.name,
                cluster_name="str",
                database_name="str",
                parameters={"ids": ["str"]},
                api_version="2024-09-01-preview",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_begin_force_link_to_replication_group(self, resource_group):
        response = await (
            await self.client.databases.begin_force_link_to_replication_group(
                resource_group_name=resource_group.name,
                cluster_name="str",
                database_name="str",
                parameters={"groupNickname": "str", "linkedDatabases": [{"id": "str", "state": "str"}]},
                api_version="2024-09-01-preview",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_begin_flush(self, resource_group):
        response = await (
            await self.client.databases.begin_flush(
                resource_group_name=resource_group.name,
                cluster_name="str",
                database_name="str",
                parameters={"ids": ["str"]},
                api_version="2024-09-01-preview",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_begin_upgrade_db_redis_version(self, resource_group):
        response = await (
            await self.client.databases.begin_upgrade_db_redis_version(
                resource_group_name=resource_group.name,
                cluster_name="str",
                database_name="str",
                api_version="2024-09-01-preview",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...
