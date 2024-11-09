# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.netapp.aio import NetAppManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer
from devtools_testutils.aio import recorded_by_proxy_async

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestNetAppManagementBackupsOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(NetAppManagementClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_get_latest_status(self, resource_group):
        response = await self.client.backups.get_latest_status(
            resource_group_name=resource_group.name,
            account_name="str",
            pool_name="str",
            volume_name="str",
            api_version="2024-07-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_get_volume_latest_restore_status(self, resource_group):
        response = await self.client.backups.get_volume_latest_restore_status(
            resource_group_name=resource_group.name,
            account_name="str",
            pool_name="str",
            volume_name="str",
            api_version="2024-07-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_list_by_vault(self, resource_group):
        response = self.client.backups.list_by_vault(
            resource_group_name=resource_group.name,
            account_name="str",
            backup_vault_name="str",
            api_version="2024-07-01",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_get(self, resource_group):
        response = await self.client.backups.get(
            resource_group_name=resource_group.name,
            account_name="str",
            backup_vault_name="str",
            backup_name="str",
            api_version="2024-07-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_begin_create(self, resource_group):
        response = await (
            await self.client.backups.begin_create(
                resource_group_name=resource_group.name,
                account_name="str",
                backup_vault_name="str",
                backup_name="str",
                body={
                    "volumeResourceId": "str",
                    "backupId": "str",
                    "backupPolicyResourceId": "str",
                    "backupType": "str",
                    "creationDate": "2020-02-20 00:00:00",
                    "failureReason": "str",
                    "id": "str",
                    "label": "str",
                    "name": "str",
                    "provisioningState": "str",
                    "size": 0,
                    "snapshotName": "str",
                    "systemData": {
                        "createdAt": "2020-02-20 00:00:00",
                        "createdBy": "str",
                        "createdByType": "str",
                        "lastModifiedAt": "2020-02-20 00:00:00",
                        "lastModifiedBy": "str",
                        "lastModifiedByType": "str",
                    },
                    "type": "str",
                    "useExistingSnapshot": False,
                },
                api_version="2024-07-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_begin_update(self, resource_group):
        response = await (
            await self.client.backups.begin_update(
                resource_group_name=resource_group.name,
                account_name="str",
                backup_vault_name="str",
                backup_name="str",
                api_version="2024-07-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_begin_delete(self, resource_group):
        response = await (
            await self.client.backups.begin_delete(
                resource_group_name=resource_group.name,
                account_name="str",
                backup_vault_name="str",
                backup_name="str",
                api_version="2024-07-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...
