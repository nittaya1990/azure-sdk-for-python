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
    python dataflow_create_or_update_complex_contextualization.py

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

    response = client.dataflow.begin_create_or_update(
        resource_group_name="rgiotoperations",
        instance_name="resource-name123",
        dataflow_profile_name="resource-name123",
        dataflow_name="aio-to-adx-contexualized",
        resource={
            "extendedLocation": {"name": "qmbrfwcpwwhggszhrdjv", "type": "CustomLocation"},
            "properties": {
                "mode": "Enabled",
                "operations": [
                    {
                        "name": "source1",
                        "operationType": "Source",
                        "sourceSettings": {
                            "dataSources": ["azure-iot-operations/data/thermostat"],
                            "endpointRef": "aio-builtin-broker-endpoint",
                        },
                    },
                    {
                        "builtInTransformationSettings": {
                            "datasets": [
                                {
                                    "expression": "$1 == $2",
                                    "inputs": ["$source.country", "$context.country"],
                                    "key": "quality",
                                }
                            ],
                            "map": [
                                {"inputs": ["*"], "output": "*"},
                                {"inputs": ["$context(quality).*"], "output": "enriched.*"},
                            ],
                        },
                        "name": "transformation1",
                        "operationType": "BuiltInTransformation",
                    },
                    {
                        "destinationSettings": {"dataDestination": "mytable", "endpointRef": "adx-endpoint"},
                        "name": "destination1",
                        "operationType": "Destination",
                    },
                ],
            },
        },
    ).result()
    print(response)


# x-ms-original-file: 2024-11-01/Dataflow_CreateOrUpdate_ComplexContextualization.json
if __name__ == "__main__":
    main()
