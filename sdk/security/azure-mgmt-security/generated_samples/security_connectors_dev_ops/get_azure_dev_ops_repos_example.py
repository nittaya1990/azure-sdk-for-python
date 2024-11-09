# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential

from azure.mgmt.security import SecurityCenter

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-security
# USAGE
    python get_azure_dev_ops_repos_example.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = SecurityCenter(
        credential=DefaultAzureCredential(),
        subscription_id="0806e1cd-cfda-4ff8-b99c-2b0af42cffd3",
    )

    response = client.azure_dev_ops_repos.get(
        resource_group_name="myRg",
        security_connector_name="mySecurityConnectorName",
        org_name="myAzDevOpsOrg",
        project_name="myAzDevOpsProject",
        repo_name="myAzDevOpsRepo",
    )
    print(response)


# x-ms-original-file: specification/security/resource-manager/Microsoft.Security/stable/2024-04-01/examples/SecurityConnectorsDevOps/GetAzureDevOpsRepos_example.json
if __name__ == "__main__":
    main()
