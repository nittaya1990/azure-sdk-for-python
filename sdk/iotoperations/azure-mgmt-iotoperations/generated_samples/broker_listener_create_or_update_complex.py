# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential

from azure.mgmt.iotoperations import IoTOperationsMgmtClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-iotoperations
# USAGE
    python broker_listener_create_or_update_complex.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = IoTOperationsMgmtClient(
        credential=DefaultAzureCredential(),
        subscription_id="SUBSCRIPTION_ID",
    )

    response = client.broker_listener.begin_create_or_update(
        resource_group_name="rgiotoperations",
        instance_name="resource-name123",
        broker_name="resource-name123",
        listener_name="resource-name123",
        resource={
            "extendedLocation": {"name": "qmbrfwcpwwhggszhrdjv", "type": "CustomLocation"},
            "properties": {
                "ports": [
                    {"authenticationRef": "example-authentication", "port": 8080, "protocol": "WebSockets"},
                    {
                        "authenticationRef": "example-authentication",
                        "port": 8443,
                        "protocol": "WebSockets",
                        "tls": {
                            "certManagerCertificateSpec": {
                                "issuerRef": {
                                    "group": "jtmuladdkpasfpoyvewekmiy",
                                    "kind": "Issuer",
                                    "name": "example-issuer",
                                }
                            },
                            "mode": "Automatic",
                        },
                    },
                    {"authenticationRef": "example-authentication", "port": 1883},
                    {
                        "authenticationRef": "example-authentication",
                        "port": 8883,
                        "tls": {"manual": {"secretRef": "example-secret"}, "mode": "Manual"},
                    },
                ],
                "serviceType": "LoadBalancer",
            },
        },
    ).result()
    print(response)


# x-ms-original-file: 2024-09-15-preview/BrokerListener_CreateOrUpdate_Complex.json
if __name__ == "__main__":
    main()
