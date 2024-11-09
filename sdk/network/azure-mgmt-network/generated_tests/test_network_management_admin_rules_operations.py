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
class TestNetworkManagementAdminRulesOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(NetworkManagementClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list(self, resource_group):
        response = self.client.admin_rules.list(
            resource_group_name=resource_group.name,
            network_manager_name="str",
            configuration_name="str",
            rule_collection_name="str",
            api_version="2024-03-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_get(self, resource_group):
        response = self.client.admin_rules.get(
            resource_group_name=resource_group.name,
            network_manager_name="str",
            configuration_name="str",
            rule_collection_name="str",
            rule_name="str",
            api_version="2024-03-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_create_or_update(self, resource_group):
        response = self.client.admin_rules.create_or_update(
            resource_group_name=resource_group.name,
            network_manager_name="str",
            configuration_name="str",
            rule_collection_name="str",
            rule_name="str",
            admin_rule={
                "kind": "Custom",
                "access": "str",
                "description": "str",
                "destinationPortRanges": ["str"],
                "destinations": [{"addressPrefix": "str", "addressPrefixType": "str"}],
                "direction": "str",
                "etag": "str",
                "id": "str",
                "name": "str",
                "priority": 0,
                "protocol": "str",
                "provisioningState": "str",
                "resourceGuid": "str",
                "sourcePortRanges": ["str"],
                "sources": [{"addressPrefix": "str", "addressPrefixType": "str"}],
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
            api_version="2024-03-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_delete(self, resource_group):
        response = self.client.admin_rules.begin_delete(
            resource_group_name=resource_group.name,
            network_manager_name="str",
            configuration_name="str",
            rule_collection_name="str",
            rule_name="str",
            api_version="2024-03-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...
