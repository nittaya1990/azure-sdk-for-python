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
    python dataflow_endpoint_create_or_update_kafka.py

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

    response = client.dataflow_endpoint.begin_create_or_update(
        resource_group_name="rgiotoperations",
        instance_name="resource-name123",
        dataflow_endpoint_name="generic-kafka-endpoint",
        resource={
            "extendedLocation": {"name": "qmbrfwcpwwhggszhrdjv", "type": "CustomLocation"},
            "properties": {
                "endpointType": "Kafka",
                "kafkaSettings": {
                    "authentication": {
                        "method": "Sasl",
                        "saslSettings": {"saslType": "Plain", "secretRef": "my-secret"},
                    },
                    "batching": {"latencyMs": 5, "maxBytes": 1000000, "maxMessages": 100000, "mode": "Enabled"},
                    "cloudEventAttributes": "Propagate",
                    "compression": "Gzip",
                    "consumerGroupId": "dataflows",
                    "copyMqttProperties": "Enabled",
                    "host": "example.kafka.local:9093",
                    "kafkaAcks": "All",
                    "partitionStrategy": "Default",
                    "tls": {"mode": "Enabled", "trustedCaCertificateConfigMapRef": "ca-certificates"},
                },
            },
        },
    ).result()
    print(response)


# x-ms-original-file: 2024-09-15-preview/DataflowEndpoint_CreateOrUpdate_Kafka.json
if __name__ == "__main__":
    main()
