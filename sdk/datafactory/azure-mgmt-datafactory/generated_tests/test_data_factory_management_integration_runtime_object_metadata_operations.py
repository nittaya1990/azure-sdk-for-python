# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.datafactory import DataFactoryManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestDataFactoryManagementIntegrationRuntimeObjectMetadataOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(DataFactoryManagementClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_refresh(self, resource_group):
        response = self.client.integration_runtime_object_metadata.begin_refresh(
            resource_group_name=resource_group.name,
            factory_name="str",
            integration_runtime_name="str",
            api_version="2018-06-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_get(self, resource_group):
        response = self.client.integration_runtime_object_metadata.get(
            resource_group_name=resource_group.name,
            factory_name="str",
            integration_runtime_name="str",
            api_version="2018-06-01",
        )

        # please add some check logic here by yourself
        # ...
