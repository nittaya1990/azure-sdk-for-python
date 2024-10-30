# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential

from azure.mgmt.edgeorder import EdgeOrderManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-edgeorder
# USAGE
    python update_address.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = EdgeOrderManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="YourSubscriptionId",
    )

    response = client.begin_update_address(
        address_name="TestAddressName2",
        resource_group_name="YourResourceGroupName",
        address_update_parameter={
            "properties": {
                "contactDetails": {
                    "contactName": "YYYY YYYY",
                    "emailList": ["xxxx@xxxx.xxx"],
                    "phone": "0000000000",
                    "phoneExtension": "",
                },
                "shippingAddress": {
                    "addressType": "None",
                    "city": "San Francisco",
                    "companyName": "Microsoft",
                    "country": "US",
                    "postalCode": "94107",
                    "stateOrProvince": "CA",
                    "streetAddress1": "16 TOWNSEND ST",
                    "streetAddress2": "UNIT 1",
                },
            },
            "tags": {"tag1": "value1", "tag2": "value2"},
        },
    ).result()
    print(response)


# x-ms-original-file: specification/edgeorder/resource-manager/Microsoft.EdgeOrder/stable/2021-12-01/examples/UpdateAddress.json
if __name__ == "__main__":
    main()
