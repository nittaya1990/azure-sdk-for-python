# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential

from azure.mgmt.cosmosdb import CosmosDBManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-cosmosdb
# USAGE
    python cosmos_db_data_transfer_job_create.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = CosmosDBManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="subid",
    )

    response = client.data_transfer_jobs.create(
        resource_group_name="rg1",
        account_name="ddb1",
        job_name="j1",
        job_create_parameters={
            "properties": {
                "destination": {
                    "component": "AzureBlobStorage",
                    "containerName": "blob_container",
                    "endpointUrl": "https://blob.windows.net",
                },
                "source": {"component": "CosmosDBCassandra", "keyspaceName": "keyspace", "tableName": "table"},
            }
        },
    )
    print(response)


# x-ms-original-file: specification/cosmos-db/resource-manager/Microsoft.DocumentDB/preview/2024-09-01-preview/examples/data-transfer-service/CosmosDBDataTransferJobCreate.json
if __name__ == "__main__":
    main()
