# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.loganalytics import LogAnalyticsManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestLogAnalyticsManagementLinkedStorageAccountsOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(LogAnalyticsManagementClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_create_or_update(self, resource_group):
        response = self.client.linked_storage_accounts.create_or_update(
            resource_group_name=resource_group.name,
            workspace_name="str",
            data_source_type="str",
            parameters={
                "dataSourceType": "str",
                "id": "str",
                "name": "str",
                "storageAccountIds": ["str"],
                "type": "str",
            },
            api_version="2020-08-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_delete(self, resource_group):
        response = self.client.linked_storage_accounts.delete(
            resource_group_name=resource_group.name,
            workspace_name="str",
            data_source_type="str",
            api_version="2020-08-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_get(self, resource_group):
        response = self.client.linked_storage_accounts.get(
            resource_group_name=resource_group.name,
            workspace_name="str",
            data_source_type="str",
            api_version="2020-08-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list_by_workspace(self, resource_group):
        response = self.client.linked_storage_accounts.list_by_workspace(
            resource_group_name=resource_group.name,
            workspace_name="str",
            api_version="2020-08-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...
