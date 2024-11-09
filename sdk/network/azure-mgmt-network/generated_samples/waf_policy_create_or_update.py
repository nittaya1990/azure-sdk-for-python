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
    python waf_policy_create_or_update.py

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

    response = client.web_application_firewall_policies.create_or_update(
        resource_group_name="rg1",
        policy_name="Policy1",
        parameters={
            "location": "WestUs",
            "properties": {
                "customRules": [
                    {
                        "action": "Block",
                        "matchConditions": [
                            {
                                "matchValues": ["192.168.1.0/24", "10.0.0.0/24"],
                                "matchVariables": [{"selector": None, "variableName": "RemoteAddr"}],
                                "operator": "IPMatch",
                            }
                        ],
                        "name": "Rule1",
                        "priority": 1,
                        "ruleType": "MatchRule",
                    },
                    {
                        "action": "Block",
                        "matchConditions": [
                            {
                                "matchValues": ["192.168.1.0/24"],
                                "matchVariables": [{"selector": None, "variableName": "RemoteAddr"}],
                                "operator": "IPMatch",
                            },
                            {
                                "matchValues": ["Windows"],
                                "matchVariables": [{"selector": "UserAgent", "variableName": "RequestHeaders"}],
                                "operator": "Contains",
                            },
                        ],
                        "name": "Rule2",
                        "priority": 2,
                        "ruleType": "MatchRule",
                    },
                    {
                        "action": "Block",
                        "groupByUserSession": [{"groupByVariables": [{"variableName": "ClientAddr"}]}],
                        "matchConditions": [
                            {
                                "matchValues": ["192.168.1.0/24", "10.0.0.0/24"],
                                "matchVariables": [{"selector": None, "variableName": "RemoteAddr"}],
                                "negationConditon": True,
                                "operator": "IPMatch",
                            }
                        ],
                        "name": "RateLimitRule3",
                        "priority": 3,
                        "rateLimitDuration": "OneMin",
                        "rateLimitThreshold": 10,
                        "ruleType": "RateLimitRule",
                    },
                    {
                        "action": "JSChallenge",
                        "matchConditions": [
                            {
                                "matchValues": ["192.168.1.0/24"],
                                "matchVariables": [{"selector": None, "variableName": "RemoteAddr"}],
                                "operator": "IPMatch",
                            },
                            {
                                "matchValues": ["Bot"],
                                "matchVariables": [{"selector": "UserAgent", "variableName": "RequestHeaders"}],
                                "operator": "Contains",
                            },
                        ],
                        "name": "Rule4",
                        "priority": 4,
                        "ruleType": "MatchRule",
                    },
                ],
                "managedRules": {
                    "exceptions": [
                        {
                            "exceptionManagedRuleSets": [{"ruleSetType": "OWASP", "ruleSetVersion": "3.2"}],
                            "matchVariable": "RequestURI",
                            "valueMatchOperator": "Contains",
                            "values": ["health", "account/images", "default.aspx"],
                        },
                        {
                            "exceptionManagedRuleSets": [
                                {
                                    "ruleGroups": [{"ruleGroupName": "REQUEST-932-APPLICATION-ATTACK-RCE"}],
                                    "ruleSetType": "OWASP",
                                    "ruleSetVersion": "3.2",
                                }
                            ],
                            "matchVariable": "RequestHeader",
                            "selector": "User-Agent",
                            "selectorMatchOperator": "StartsWith",
                            "valueMatchOperator": "Contains",
                            "values": ["Mozilla/5.0", "Chrome/122.0.0.0"],
                        },
                        {
                            "exceptionManagedRuleSets": [
                                {
                                    "ruleGroups": [{"ruleGroupName": "BadBots", "rules": [{"ruleId": "100100"}]}],
                                    "ruleSetType": "Microsoft_BotManagerRuleSet",
                                    "ruleSetVersion": "1.0",
                                }
                            ],
                            "matchVariable": "RemoteAddr",
                            "valueMatchOperator": "IPMatch",
                            "values": ["1.2.3.4", "10.0.0.1/6"],
                        },
                    ],
                    "exclusions": [
                        {
                            "exclusionManagedRuleSets": [
                                {
                                    "ruleGroups": [
                                        {
                                            "ruleGroupName": "REQUEST-930-APPLICATION-ATTACK-LFI",
                                            "rules": [{"ruleId": "930120"}],
                                        },
                                        {"ruleGroupName": "REQUEST-932-APPLICATION-ATTACK-RCE"},
                                    ],
                                    "ruleSetType": "OWASP",
                                    "ruleSetVersion": "3.2",
                                }
                            ],
                            "matchVariable": "RequestArgNames",
                            "selector": "hello",
                            "selectorMatchOperator": "StartsWith",
                        },
                        {
                            "exclusionManagedRuleSets": [
                                {"ruleGroups": [], "ruleSetType": "OWASP", "ruleSetVersion": "3.1"}
                            ],
                            "matchVariable": "RequestArgNames",
                            "selector": "hello",
                            "selectorMatchOperator": "EndsWith",
                        },
                        {"matchVariable": "RequestArgNames", "selector": "test", "selectorMatchOperator": "StartsWith"},
                        {
                            "matchVariable": "RequestArgValues",
                            "selector": "test",
                            "selectorMatchOperator": "StartsWith",
                        },
                    ],
                    "managedRuleSets": [
                        {
                            "ruleGroupOverrides": [
                                {
                                    "ruleGroupName": "REQUEST-931-APPLICATION-ATTACK-RFI",
                                    "rules": [
                                        {"action": "Log", "ruleId": "931120", "state": "Enabled"},
                                        {"action": "AnomalyScoring", "ruleId": "931130", "state": "Disabled"},
                                    ],
                                }
                            ],
                            "ruleSetType": "OWASP",
                            "ruleSetVersion": "3.2",
                        },
                        {
                            "ruleGroupOverrides": [
                                {
                                    "ruleGroupName": "UnknownBots",
                                    "rules": [{"action": "JSChallenge", "ruleId": "300700", "state": "Enabled"}],
                                }
                            ],
                            "ruleSetType": "Microsoft_BotManagerRuleSet",
                            "ruleSetVersion": "1.0",
                        },
                        {
                            "ruleGroupOverrides": [
                                {
                                    "ruleGroupName": "ExcessiveRequests",
                                    "rules": [
                                        {
                                            "action": "Block",
                                            "ruleId": "500100",
                                            "sensitivity": "High",
                                            "state": "Enabled",
                                        }
                                    ],
                                }
                            ],
                            "ruleSetType": "Microsoft_HTTPDDoSRuleSet",
                            "ruleSetVersion": "1.0",
                        },
                    ],
                },
                "policySettings": {
                    "jsChallengeCookieExpirationInMins": 100,
                    "logScrubbing": {
                        "scrubbingRules": [
                            {
                                "matchVariable": "RequestArgNames",
                                "selector": "test",
                                "selectorMatchOperator": "Equals",
                                "state": "Enabled",
                            },
                            {
                                "matchVariable": "RequestIPAddress",
                                "selectorMatchOperator": "EqualsAny",
                                "state": "Enabled",
                            },
                        ],
                        "state": "Enabled",
                    },
                },
            },
        },
    )
    print(response)


# x-ms-original-file: specification/network/resource-manager/Microsoft.Network/stable/2024-03-01/examples/WafPolicyCreateOrUpdate.json
if __name__ == "__main__":
    main()
