# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.network import NetworkManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestNetworkManagementRoutesOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(NetworkManagementClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_delete(self, resource_group):
        response = self.client.routes.begin_delete(
            resource_group_name=resource_group.name,
            route_table_name="str",
            route_name="str",
            api_version="2024-03-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_get(self, resource_group):
        response = self.client.routes.get(
            resource_group_name=resource_group.name,
            route_table_name="str",
            route_name="str",
            api_version="2024-03-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_create_or_update(self, resource_group):
        response = self.client.routes.begin_create_or_update(
            resource_group_name=resource_group.name,
            route_table_name="str",
            route_name="str",
            route_parameters={
                "addressPrefix": "str",
                "etag": "str",
                "hasBgpOverride": bool,
                "id": "str",
                "name": "str",
                "nextHopIpAddress": "str",
                "nextHopType": "str",
                "provisioningState": "str",
                "type": "str",
            },
            api_version="2024-03-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list(self, resource_group):
        response = self.client.routes.list(
            resource_group_name=resource_group.name,
            route_table_name="str",
            api_version="2024-03-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...
