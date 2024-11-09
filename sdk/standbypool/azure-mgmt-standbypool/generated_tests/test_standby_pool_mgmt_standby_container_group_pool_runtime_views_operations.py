# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.standbypool import StandbyPoolMgmtClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestStandbyPoolMgmtStandbyContainerGroupPoolRuntimeViewsOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(StandbyPoolMgmtClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_standby_container_group_pool_runtime_views_get(self, resource_group):
        response = self.client.standby_container_group_pool_runtime_views.get(
            resource_group_name=resource_group.name,
            standby_container_group_pool_name="str",
            runtime_view="str",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_standby_container_group_pool_runtime_views_list_by_standby_pool(self, resource_group):
        response = self.client.standby_container_group_pool_runtime_views.list_by_standby_pool(
            resource_group_name=resource_group.name,
            standby_container_group_pool_name="str",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...
