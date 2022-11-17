# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.iothubprovisioningservices import IotDpsClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-iothubprovisioningservices
# USAGE
    python dps_create.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = IotDpsClient(
        credential=DefaultAzureCredential(),
        subscription_id="91d12660-3dec-467a-be2a-213b5544ddc0",
    )

    response = client.iot_dps_resource.begin_create_or_update(
        resource_group_name="myResourceGroup",
        provisioning_service_name="myFirstProvisioningService",
        iot_dps_description={
            "location": "East US",
            "properties": {"enableDataResidency": False},
            "sku": {"capacity": 1, "name": "S1"},
            "tags": {},
        },
    ).result()
    print(response)


# x-ms-original-file: specification/deviceprovisioningservices/resource-manager/Microsoft.Devices/stable/2022-02-05/examples/DPSCreate.json
if __name__ == "__main__":
    main()
