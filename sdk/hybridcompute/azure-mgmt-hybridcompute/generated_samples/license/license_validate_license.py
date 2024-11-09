# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential

from azure.mgmt.hybridcompute import HybridComputeManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-hybridcompute
# USAGE
    python license_validate_license.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = HybridComputeManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="{subscriptionId}",
    )

    response = client.licenses.begin_validate_license(
        parameters={
            "location": "eastus2euap",
            "properties": {
                "licenseDetails": {
                    "edition": "Datacenter",
                    "processors": 6,
                    "state": "Activated",
                    "target": "Windows Server 2012",
                    "type": "pCore",
                },
                "licenseType": "ESU",
            },
        },
    ).result()
    print(response)


# x-ms-original-file: specification/hybridcompute/resource-manager/Microsoft.HybridCompute/stable/2024-07-10/examples/license/License_ValidateLicense.json
if __name__ == "__main__":
    main()
