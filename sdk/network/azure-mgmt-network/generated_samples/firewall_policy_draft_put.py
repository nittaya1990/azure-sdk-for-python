# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential

from azure.mgmt.network import NetworkManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-network
# USAGE
    python firewall_policy_draft_put.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = NetworkManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="subid",
    )

    response = client.firewall_policy_drafts.create_or_update(
        resource_group_name="rg1",
        firewall_policy_name="firewallPolicy",
        parameters={
            "properties": {
                "dnsSettings": {"enableProxy": True, "requireProxyForNetworkRules": False, "servers": ["30.3.4.5"]},
                "explicitProxy": {
                    "enableExplicitProxy": True,
                    "enablePacFile": True,
                    "httpPort": 8087,
                    "httpsPort": 8087,
                    "pacFile": "https://tinawstorage.file.core.windows.net/?sv=2020-02-10&ss=bfqt&srt=sco&sp=rwdlacuptfx&se=2021-06-04T07:01:12Z&st=2021-06-03T23:01:12Z&sip=68.65.171.11&spr=https&sig=Plsa0RRVpGbY0IETZZOT6znOHcSro71LLTTbzquYPgs%3D",
                    "pacFilePort": 8087,
                },
                "insights": {
                    "isEnabled": True,
                    "logAnalyticsResources": {
                        "defaultWorkspaceId": {
                            "id": "/subscriptions/subid/resourcegroups/rg1/providers/microsoft.operationalinsights/workspaces/defaultWorkspace"
                        },
                        "workspaces": [
                            {
                                "region": "westus",
                                "workspaceId": {
                                    "id": "/subscriptions/subid/resourcegroups/rg1/providers/microsoft.operationalinsights/workspaces/workspace1"
                                },
                            },
                            {
                                "region": "eastus",
                                "workspaceId": {
                                    "id": "/subscriptions/subid/resourcegroups/rg1/providers/microsoft.operationalinsights/workspaces/workspace2"
                                },
                            },
                        ],
                    },
                    "retentionDays": 100,
                },
                "intrusionDetection": {
                    "configuration": {
                        "bypassTrafficSettings": [
                            {
                                "description": "Rule 1",
                                "destinationAddresses": ["5.6.7.8"],
                                "destinationPorts": ["*"],
                                "name": "bypassRule1",
                                "protocol": "TCP",
                                "sourceAddresses": ["1.2.3.4"],
                            }
                        ],
                        "signatureOverrides": [{"id": "2525004", "mode": "Deny"}],
                    },
                    "mode": "Alert",
                    "profile": "Balanced",
                },
                "snat": {"privateRanges": ["IANAPrivateRanges"]},
                "sql": {"allowSqlRedirect": True},
                "threatIntelMode": "Alert",
                "threatIntelWhitelist": {"fqdns": ["*.microsoft.com"], "ipAddresses": ["20.3.4.5"]},
            }
        },
    )
    print(response)


# x-ms-original-file: specification/network/resource-manager/Microsoft.Network/stable/2024-03-01/examples/FirewallPolicyDraftPut.json
if __name__ == "__main__":
    main()
