# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.eventhub import EventHubManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-eventhub
# USAGE
    python eh_name_space_authorization_rule_create.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = EventHubManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="5f750a97-50d9-4e36-8081-c9ee4c0210d4",
    )

    response = client.namespaces.create_or_update_authorization_rule(
        resource_group_name="ArunMonocle",
        namespace_name="sdk-Namespace-2702",
        authorization_rule_name="sdk-Authrules-1746",
        parameters={"properties": {"rights": ["Listen", "Send"]}},
    )
    print(response)


# x-ms-original-file: specification/eventhub/resource-manager/Microsoft.EventHub/stable/2021-11-01/examples/NameSpaces/EHNameSpaceAuthorizationRuleCreate.json
if __name__ == "__main__":
    main()
