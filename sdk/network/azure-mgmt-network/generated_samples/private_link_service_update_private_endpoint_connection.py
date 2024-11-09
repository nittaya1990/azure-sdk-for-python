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
    python private_link_service_update_private_endpoint_connection.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = NetworkManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="subId",
    )

    response = client.private_link_services.update_private_endpoint_connection(
        resource_group_name="rg1",
        service_name="testPls",
        pe_connection_name="testPlePeConnection",
        parameters={
            "name": "testPlePeConnection",
            "properties": {
                "privateEndpoint": {
                    "id": "/subscriptions/subId/resourceGroups/rg1/providers/Microsoft.Network/privateEndpoints/testPe"
                },
                "privateLinkServiceConnectionState": {
                    "description": "approved it for some reason.",
                    "status": "Approved",
                },
            },
        },
    )
    print(response)


# x-ms-original-file: specification/network/resource-manager/Microsoft.Network/stable/2024-03-01/examples/PrivateLinkServiceUpdatePrivateEndpointConnection.json
if __name__ == "__main__":
    main()
