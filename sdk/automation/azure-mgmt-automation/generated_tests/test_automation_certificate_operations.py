# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.automation import AutomationClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestAutomationCertificateOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(AutomationClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_delete(self, resource_group):
        response = self.client.certificate.delete(
            resource_group_name=resource_group.name,
            automation_account_name="str",
            certificate_name="str",
            api_version="2022-08-08",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_get(self, resource_group):
        response = self.client.certificate.get(
            resource_group_name=resource_group.name,
            automation_account_name="str",
            certificate_name="str",
            api_version="2022-08-08",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_create_or_update(self, resource_group):
        response = self.client.certificate.create_or_update(
            resource_group_name=resource_group.name,
            automation_account_name="str",
            certificate_name="str",
            parameters={
                "base64Value": "str",
                "name": "str",
                "description": "str",
                "isExportable": bool,
                "thumbprint": "str",
            },
            api_version="2022-08-08",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_update(self, resource_group):
        response = self.client.certificate.update(
            resource_group_name=resource_group.name,
            automation_account_name="str",
            certificate_name="str",
            parameters={"description": "str", "name": "str"},
            api_version="2022-08-08",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list_by_automation_account(self, resource_group):
        response = self.client.certificate.list_by_automation_account(
            resource_group_name=resource_group.name,
            automation_account_name="str",
            api_version="2022-08-08",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...
