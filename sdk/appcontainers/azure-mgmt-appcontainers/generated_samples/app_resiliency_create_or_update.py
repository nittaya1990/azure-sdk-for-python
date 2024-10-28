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
    python app_resiliency_create_or_update.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = ContainerAppsAPIClient(
        credential=DefaultAzureCredential(),
        subscription_id="34adfa4f-cedf-4dc0-ba29-b6d1a69ab345",
    )

    response = client.app_resiliency.create_or_update(
        resource_group_name="rg",
        app_name="testcontainerApp0",
        name="resiliency-policy-1",
        resiliency_envelope={
            "properties": {
                "circuitBreakerPolicy": {"consecutiveErrors": 5, "intervalInSeconds": 10, "maxEjectionPercent": 50},
                "httpConnectionPool": {"http1MaxPendingRequests": 1024, "http2MaxRequests": 1024},
                "httpRetryPolicy": {
                    "matches": {
                        "errors": ["5xx", "connect-failure", "reset", "retriable-headers", "retriable-status-codes"],
                        "headers": [{"header": "X-Content-Type", "match": {"prefixMatch": "GOATS"}}],
                        "httpStatusCodes": [502, 503],
                    },
                    "maxRetries": 5,
                    "retryBackOff": {"initialDelayInMilliseconds": 1000, "maxIntervalInMilliseconds": 10000},
                },
                "tcpConnectionPool": {"maxConnections": 100},
                "tcpRetryPolicy": {"maxConnectAttempts": 3},
                "timeoutPolicy": {"connectionTimeoutInSeconds": 5, "responseTimeoutInSeconds": 15},
            }
        },
    )
    print(response)


# x-ms-original-file: specification/app/resource-manager/Microsoft.App/preview/2024-08-02-preview/examples/AppResiliency_CreateOrUpdate.json
if __name__ == "__main__":
    main()
