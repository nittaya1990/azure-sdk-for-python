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
    python java_components_patch_service_bind.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = ContainerAppsAPIClient(
        credential=DefaultAzureCredential(),
        subscription_id="8efdecc5-919e-44eb-b179-915dca89ebf9",
    )

    response = client.java_components.begin_update(
        resource_group_name="examplerg",
        environment_name="myenvironment",
        name="myjavacomponent",
        java_component_envelope={
            "properties": {
                "componentType": "SpringBootAdmin",
                "configurations": [
                    {"propertyName": "spring.boot.admin.ui.enable-toasts", "value": "true"},
                    {"propertyName": "spring.boot.admin.monitor.status-interval", "value": "10000ms"},
                ],
                "scale": {"maxReplicas": 1, "minReplicas": 1},
                "serviceBinds": [
                    {
                        "name": "yellowcat",
                        "serviceId": "/subscriptions/8efdecc5-919e-44eb-b179-915dca89ebf9/resourceGroups/examplerg/providers/Microsoft.App/managedEnvironments/myenvironment/javaComponents/yellowcat",
                    }
                ],
            }
        },
    ).result()
    print(response)


# x-ms-original-file: specification/app/resource-manager/Microsoft.App/preview/2024-08-02-preview/examples/JavaComponents_Patch_ServiceBind.json
if __name__ == "__main__":
    main()
