# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential

from azure.mgmt.dns import DnsManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-dns
# USAGE
    python create_or_update_arecordset_alias.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = DnsManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="subid",
    )

    response = client.record_sets.create_or_update(
        resource_group_name="rg1",
        zone_name="zone1",
        relative_record_set_name="record1",
        record_type="A",
        parameters={
            "properties": {
                "TTL": 3600,
                "metadata": {"key1": "value1"},
                "targetResource": {
                    "id": "/subscriptions/726f8cd6-6459-4db4-8e6d-2cd2716904e2/resourceGroups/test/providers/Microsoft.Network/trafficManagerProfiles/testpp2"
                },
            }
        },
    )
    print(response)


# x-ms-original-file: specification/dns/resource-manager/Microsoft.Network/stable/2018-05-01/examples/CreateOrUpdateARecordsetAlias.json
if __name__ == "__main__":
    main()
