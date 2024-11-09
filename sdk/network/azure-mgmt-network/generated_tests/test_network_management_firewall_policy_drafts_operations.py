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
class TestNetworkManagementFirewallPolicyDraftsOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(NetworkManagementClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_create_or_update(self, resource_group):
        response = self.client.firewall_policy_drafts.create_or_update(
            resource_group_name=resource_group.name,
            firewall_policy_name="str",
            parameters={
                "basePolicy": {"id": "str"},
                "dnsSettings": {"enableProxy": bool, "requireProxyForNetworkRules": bool, "servers": ["str"]},
                "explicitProxy": {
                    "enableExplicitProxy": bool,
                    "enablePacFile": bool,
                    "httpPort": 0,
                    "httpsPort": 0,
                    "pacFile": "str",
                    "pacFilePort": 0,
                },
                "id": "str",
                "insights": {
                    "isEnabled": bool,
                    "logAnalyticsResources": {
                        "defaultWorkspaceId": {"id": "str"},
                        "workspaces": [{"region": "str", "workspaceId": {"id": "str"}}],
                    },
                    "retentionDays": 0,
                },
                "intrusionDetection": {
                    "configuration": {
                        "bypassTrafficSettings": [
                            {
                                "description": "str",
                                "destinationAddresses": ["str"],
                                "destinationIpGroups": ["str"],
                                "destinationPorts": ["str"],
                                "name": "str",
                                "protocol": "str",
                                "sourceAddresses": ["str"],
                                "sourceIpGroups": ["str"],
                            }
                        ],
                        "privateRanges": ["str"],
                        "signatureOverrides": [{"id": "str", "mode": "str"}],
                    },
                    "mode": "str",
                    "profile": "str",
                },
                "location": "str",
                "name": "str",
                "snat": {"autoLearnPrivateRanges": "str", "privateRanges": ["str"]},
                "sql": {"allowSqlRedirect": bool},
                "tags": {"str": "str"},
                "threatIntelMode": "str",
                "threatIntelWhitelist": {"fqdns": ["str"], "ipAddresses": ["str"]},
                "type": "str",
            },
            api_version="2024-03-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_delete(self, resource_group):
        response = self.client.firewall_policy_drafts.delete(
            resource_group_name=resource_group.name,
            firewall_policy_name="str",
            api_version="2024-03-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_get(self, resource_group):
        response = self.client.firewall_policy_drafts.get(
            resource_group_name=resource_group.name,
            firewall_policy_name="str",
            api_version="2024-03-01",
        )

        # please add some check logic here by yourself
        # ...
