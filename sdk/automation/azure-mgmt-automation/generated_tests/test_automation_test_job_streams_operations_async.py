# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.automation.aio import AutomationClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer
from devtools_testutils.aio import recorded_by_proxy_async

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestAutomationTestJobStreamsOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(AutomationClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_get(self, resource_group):
        response = await self.client.test_job_streams.get(
            resource_group_name=resource_group.name,
            automation_account_name="str",
            runbook_name="str",
            job_stream_id="str",
            api_version="2022-08-08",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_list_by_test_job(self, resource_group):
        response = self.client.test_job_streams.list_by_test_job(
            resource_group_name=resource_group.name,
            automation_account_name="str",
            runbook_name="str",
            api_version="2022-08-08",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...
