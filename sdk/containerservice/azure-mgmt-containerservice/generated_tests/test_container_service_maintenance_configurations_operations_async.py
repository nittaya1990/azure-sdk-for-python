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
class TestContainerServiceMaintenanceConfigurationsOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(ContainerServiceClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_list_by_managed_cluster(self, resource_group):
        response = self.client.maintenance_configurations.list_by_managed_cluster(
            resource_group_name=resource_group.name,
            resource_name="str",
            api_version="2024-09-01",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_get(self, resource_group):
        response = await self.client.maintenance_configurations.get(
            resource_group_name=resource_group.name,
            resource_name="str",
            config_name="str",
            api_version="2024-09-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_create_or_update(self, resource_group):
        response = await self.client.maintenance_configurations.create_or_update(
            resource_group_name=resource_group.name,
            resource_name="str",
            config_name="str",
            parameters={
                "id": "str",
                "maintenanceWindow": {
                    "durationHours": 24,
                    "schedule": {
                        "absoluteMonthly": {"dayOfMonth": 0, "intervalMonths": 0},
                        "daily": {"intervalDays": 0},
                        "relativeMonthly": {"dayOfWeek": "str", "intervalMonths": 0, "weekIndex": "str"},
                        "weekly": {"dayOfWeek": "str", "intervalWeeks": 0},
                    },
                    "startTime": "str",
                    "notAllowedDates": [{"end": "2020-02-20", "start": "2020-02-20"}],
                    "startDate": "2020-02-20",
                    "utcOffset": "str",
                },
                "name": "str",
                "notAllowedTime": [{"end": "2020-02-20 00:00:00", "start": "2020-02-20 00:00:00"}],
                "systemData": {
                    "createdAt": "2020-02-20 00:00:00",
                    "createdBy": "str",
                    "createdByType": "str",
                    "lastModifiedAt": "2020-02-20 00:00:00",
                    "lastModifiedBy": "str",
                    "lastModifiedByType": "str",
                },
                "timeInWeek": [{"day": "str", "hourSlots": [0]}],
                "type": "str",
            },
            api_version="2024-09-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_delete(self, resource_group):
        response = await self.client.maintenance_configurations.delete(
            resource_group_name=resource_group.name,
            resource_name="str",
            config_name="str",
            api_version="2024-09-01",
        )

        # please add some check logic here by yourself
        # ...
