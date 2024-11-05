# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential

from azure.mgmt.automation import AutomationClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-automation
# USAGE
    python compilation_job_stream_list.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = AutomationClient(
        credential=DefaultAzureCredential(),
        subscription_id="subid",
    )

    response = client.dsc_compilation_job_stream.list_by_job(
        resource_group_name="rg",
        automation_account_name="myAutomationAccount33",
        job_id="836d4e06-2d88-46b4-8500-7febd4906838",
    )
    print(response)


# x-ms-original-file: specification/automation/resource-manager/Microsoft.Automation/preview/2020-01-13-preview/examples/compilationJobStreamList.json
if __name__ == "__main__":
    main()
