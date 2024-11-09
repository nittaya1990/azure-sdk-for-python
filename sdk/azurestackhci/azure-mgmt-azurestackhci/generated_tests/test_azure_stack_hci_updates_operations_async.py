# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.azurestackhci.aio import AzureStackHCIClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer
from devtools_testutils.aio import recorded_by_proxy_async

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestAzureStackHCIUpdatesOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(AzureStackHCIClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_begin_post(self, resource_group):
        response = await (
            await self.client.updates.begin_post(
                resource_group_name=resource_group.name,
                cluster_name="str",
                update_name="str",
                api_version="2024-04-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_list(self, resource_group):
        response = self.client.updates.list(
            resource_group_name=resource_group.name,
            cluster_name="str",
            api_version="2024-04-01",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_begin_delete(self, resource_group):
        response = await (
            await self.client.updates.begin_delete(
                resource_group_name=resource_group.name,
                cluster_name="str",
                update_name="str",
                api_version="2024-04-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_put(self, resource_group):
        response = await self.client.updates.put(
            resource_group_name=resource_group.name,
            cluster_name="str",
            update_name="str",
            update_properties={
                "availabilityType": "str",
                "componentVersions": [{"lastUpdated": "2020-02-20 00:00:00", "packageType": "str", "version": "str"}],
                "description": "str",
                "displayName": "str",
                "healthCheckDate": "2020-02-20 00:00:00",
                "healthCheckResult": [
                    {
                        "additionalData": "str",
                        "description": "str",
                        "displayName": "str",
                        "healthCheckSource": "str",
                        "healthCheckTags": {},
                        "name": "str",
                        "remediation": "str",
                        "severity": "str",
                        "status": "str",
                        "tags": {"key": "str", "value": "str"},
                        "targetResourceID": "str",
                        "targetResourceName": "str",
                        "targetResourceType": "str",
                        "timestamp": "2020-02-20 00:00:00",
                        "title": "str",
                    }
                ],
                "healthState": "str",
                "id": "str",
                "installedDate": "2020-02-20 00:00:00",
                "location": "str",
                "minSbeVersionRequired": "str",
                "name": "str",
                "notifyMessage": "str",
                "packagePath": "str",
                "packageSizeInMb": 0.0,
                "packageType": "str",
                "prerequisites": [{"packageName": "str", "updateType": "str", "version": "str"}],
                "progressPercentage": 0.0,
                "provisioningState": "str",
                "publisher": "str",
                "rebootRequired": "str",
                "releaseLink": "str",
                "state": "str",
                "systemData": {
                    "createdAt": "2020-02-20 00:00:00",
                    "createdBy": "str",
                    "createdByType": "str",
                    "lastModifiedAt": "2020-02-20 00:00:00",
                    "lastModifiedBy": "str",
                    "lastModifiedByType": "str",
                },
                "type": "str",
                "version": "str",
            },
            api_version="2024-04-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_get(self, resource_group):
        response = await self.client.updates.get(
            resource_group_name=resource_group.name,
            cluster_name="str",
            update_name="str",
            api_version="2024-04-01",
        )

        # please add some check logic here by yourself
        # ...
