# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential

from azure.mgmt.appcontainers import ContainerAppsAPIClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-appcontainers
# USAGE
    python container_apps_kind_create_or_update.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = ContainerAppsAPIClient(
        credential=DefaultAzureCredential(),
        subscription_id="00000000-0000-0000-0000-000000000000",
    )

    response = client.container_apps.begin_create_or_update(
        resource_group_name="rg",
        container_app_name="testcontainerAppKind",
        container_app_envelope={
            "kind": "workflowapp",
            "location": "East Us",
            "managedBy": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/rg/providers/Microsoft.Web/sites/testcontainerAppKind",
            "properties": {
                "configuration": {
                    "activeRevisionsMode": "Single",
                    "ingress": {"allowInsecure": True, "external": True, "targetPort": 80},
                },
                "managedEnvironmentId": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/rg/providers/Microsoft.App/managedEnvironments/testmanagedenv3",
                "template": {
                    "containers": [
                        {
                            "image": "default/logicapps-base:latest",
                            "name": "logicapps-container",
                            "resources": {"cpu": 1, "memory": "2.0Gi"},
                        }
                    ],
                    "scale": {"cooldownPeriod": 350, "maxReplicas": 30, "minReplicas": 1, "pollingInterval": 35},
                },
            },
        },
    ).result()
    print(response)


# x-ms-original-file: specification/app/resource-manager/Microsoft.App/preview/2024-08-02-preview/examples/ContainerApps_Kind_CreateOrUpdate.json
if __name__ == "__main__":
    main()
