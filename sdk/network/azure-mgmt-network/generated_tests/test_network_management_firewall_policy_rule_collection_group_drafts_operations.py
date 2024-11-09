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
class TestNetworkManagementFirewallPolicyRuleCollectionGroupDraftsOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(NetworkManagementClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_delete(self, resource_group):
        response = self.client.firewall_policy_rule_collection_group_drafts.delete(
            resource_group_name=resource_group.name,
            firewall_policy_name="str",
            rule_collection_group_name="str",
            api_version="2024-03-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_create_or_update(self, resource_group):
        response = self.client.firewall_policy_rule_collection_group_drafts.create_or_update(
            resource_group_name=resource_group.name,
            firewall_policy_name="str",
            rule_collection_group_name="str",
            parameters={
                "id": "str",
                "name": "str",
                "priority": 0,
                "ruleCollections": ["firewall_policy_rule_collection"],
                "size": "str",
                "type": "str",
            },
            api_version="2024-03-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_get(self, resource_group):
        response = self.client.firewall_policy_rule_collection_group_drafts.get(
            resource_group_name=resource_group.name,
            firewall_policy_name="str",
            rule_collection_group_name="str",
            api_version="2024-03-01",
        )

        # please add some check logic here by yourself
        # ...
