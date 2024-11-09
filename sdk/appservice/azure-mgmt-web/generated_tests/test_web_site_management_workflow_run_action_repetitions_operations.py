# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.web import WebSiteManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestWebSiteManagementWorkflowRunActionRepetitionsOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(WebSiteManagementClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list(self, resource_group):
        response = self.client.workflow_run_action_repetitions.list(
            resource_group_name=resource_group.name,
            name="str",
            workflow_name="str",
            run_name="str",
            action_name="str",
            api_version="2023-12-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_get(self, resource_group):
        response = self.client.workflow_run_action_repetitions.get(
            resource_group_name=resource_group.name,
            name="str",
            workflow_name="str",
            run_name="str",
            action_name="str",
            repetition_name="str",
            api_version="2023-12-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list_expression_traces(self, resource_group):
        response = self.client.workflow_run_action_repetitions.list_expression_traces(
            resource_group_name=resource_group.name,
            name="str",
            workflow_name="str",
            run_name="str",
            action_name="str",
            repetition_name="str",
            api_version="2023-12-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...
