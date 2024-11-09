# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential

from azure.mgmt.managedservices import ManagedServicesClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-managedservices
# USAGE
    python delete_registration_definition.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = ManagedServicesClient(
        credential=DefaultAzureCredential(),
    )

    client.registration_definitions.delete(
        registration_definition_id="26c128c2-fefa-4340-9bb1-6e081c90ada2",
        scope="subscription/0afefe50-734e-4610-8a82-a144ahf49dea",
    )


# x-ms-original-file: specification/managedservices/resource-manager/Microsoft.ManagedServices/stable/2022-10-01/examples/DeleteRegistrationDefinition.json
if __name__ == "__main__":
    main()
