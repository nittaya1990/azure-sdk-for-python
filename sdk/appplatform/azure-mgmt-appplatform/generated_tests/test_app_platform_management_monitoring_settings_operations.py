# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.appplatform import AppPlatformManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestAppPlatformManagementMonitoringSettingsOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(AppPlatformManagementClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_get(self, resource_group):
        response = self.client.monitoring_settings.get(
            resource_group_name=resource_group.name,
            service_name="str",
            api_version="2023-12-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_update_put(self, resource_group):
        response = self.client.monitoring_settings.begin_update_put(
            resource_group_name=resource_group.name,
            service_name="str",
            monitoring_setting_resource={
                "id": "str",
                "name": "str",
                "properties": {
                    "appInsightsAgentVersions": {"java": "str"},
                    "appInsightsInstrumentationKey": "str",
                    "appInsightsSamplingRate": 0.0,
                    "error": {"code": "str", "message": "str"},
                    "provisioningState": "str",
                    "traceEnabled": bool,
                },
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
            api_version="2023-12-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_update_patch(self, resource_group):
        response = self.client.monitoring_settings.begin_update_patch(
            resource_group_name=resource_group.name,
            service_name="str",
            monitoring_setting_resource={
                "id": "str",
                "name": "str",
                "properties": {
                    "appInsightsAgentVersions": {"java": "str"},
                    "appInsightsInstrumentationKey": "str",
                    "appInsightsSamplingRate": 0.0,
                    "error": {"code": "str", "message": "str"},
                    "provisioningState": "str",
                    "traceEnabled": bool,
                },
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
            api_version="2023-12-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...
