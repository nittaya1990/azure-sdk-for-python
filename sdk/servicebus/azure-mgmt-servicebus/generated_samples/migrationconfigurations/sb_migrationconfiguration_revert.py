# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential

from azure.mgmt.servicebus import ServiceBusManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-servicebus
# USAGE
    python sb_migrationconfiguration_revert.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = ServiceBusManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="SubscriptionId",
    )

    client.migration_configs.revert(
        resource_group_name="ResourceGroup",
        namespace_name="sdk-Namespace-41",
        config_name="$default",
    )


# x-ms-original-file: specification/servicebus/resource-manager/Microsoft.ServiceBus/stable/2021-11-01/examples/Migrationconfigurations/SBMigrationconfigurationRevert.json
if __name__ == "__main__":
    main()
