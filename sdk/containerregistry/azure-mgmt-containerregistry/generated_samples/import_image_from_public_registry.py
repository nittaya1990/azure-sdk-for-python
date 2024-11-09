# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.containerregistry import ContainerRegistryManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-containerregistry
# USAGE
    python import_image_from_public_registry.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = ContainerRegistryManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="00000000-0000-0000-0000-000000000000",
    )

    client.registries.begin_import_image(
        resource_group_name="myResourceGroup",
        registry_name="myRegistry",
        parameters={
            "mode": "Force",
            "source": {"registryUri": "registry.hub.docker.com", "sourceImage": "library/hello-world"},
            "targetTags": ["targetRepository:targetTag"],
            "untaggedTargetRepositories": ["targetRepository1"],
        },
    ).result()


# x-ms-original-file: specification/containerregistry/resource-manager/Microsoft.ContainerRegistry/stable/2023-07-01/examples/ImportImageFromPublicRegistry.json
if __name__ == "__main__":
    main()
