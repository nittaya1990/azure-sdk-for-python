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
    python dscp_configuration_create.py

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

    response = client.dscp_configuration.begin_create_or_update(
        resource_group_name="rg1",
        dscp_configuration_name="mydscpconfig",
        parameters={
            "location": "eastus",
            "properties": {
                "qosDefinitionCollection": [
                    {
                        "destinationIpRanges": [{"endIP": "127.0.10.2", "startIP": "127.0.10.1"}],
                        "destinationPortRanges": [{"end": 15, "start": 15}],
                        "markings": [1],
                        "protocol": "Tcp",
                        "sourceIpRanges": [{"endIP": "127.0.0.2", "startIP": "127.0.0.1"}],
                        "sourcePortRanges": [{"end": 11, "start": 10}, {"end": 21, "start": 20}],
                    },
                    {
                        "destinationIpRanges": [{"endIP": "12.0.10.2", "startIP": "12.0.10.1"}],
                        "destinationPortRanges": [{"end": 52, "start": 51}],
                        "markings": [2],
                        "protocol": "Udp",
                        "sourceIpRanges": [{"endIP": "12.0.0.2", "startIP": "12.0.0.1"}],
                        "sourcePortRanges": [{"end": 12, "start": 11}],
                    },
                ]
            },
        },
    ).result()
    print(response)


# x-ms-original-file: specification/network/resource-manager/Microsoft.Network/stable/2024-03-01/examples/DscpConfigurationCreate.json
if __name__ == "__main__":
    main()
