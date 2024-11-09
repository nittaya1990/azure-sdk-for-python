# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.appplatform import AppPlatformManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestAppPlatformManagementApiPortalCustomDomainsOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(AppPlatformManagementClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_get(self, resource_group):
        response = self.client.api_portal_custom_domains.get(
            resource_group_name=resource_group.name,
            service_name="str",
            api_portal_name="str",
            domain_name="str",
            api_version="2023-12-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_create_or_update(self, resource_group):
        response = self.client.api_portal_custom_domains.begin_create_or_update(
            resource_group_name=resource_group.name,
            service_name="str",
            api_portal_name="str",
            domain_name="str",
            api_portal_custom_domain_resource={
                "id": "str",
                "name": "str",
                "properties": {"thumbprint": "str"},
                "systemData": {
                    "createdAt": "2020-02-20 00:00:00",
                    "createdBy": "str",
                    "createdByType": "str",
                    "lastModifiedAt": "2020-02-20 00:00:00",
                    "lastModifiedBy": "str",
                    "lastModifiedByType": "str",
                },
                "type": "str",
            },
            api_version="2023-12-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_delete(self, resource_group):
        response = self.client.api_portal_custom_domains.begin_delete(
            resource_group_name=resource_group.name,
            service_name="str",
            api_portal_name="str",
            domain_name="str",
            api_version="2023-12-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list(self, resource_group):
        response = self.client.api_portal_custom_domains.list(
            resource_group_name=resource_group.name,
            service_name="str",
            api_portal_name="str",
            api_version="2023-12-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...
