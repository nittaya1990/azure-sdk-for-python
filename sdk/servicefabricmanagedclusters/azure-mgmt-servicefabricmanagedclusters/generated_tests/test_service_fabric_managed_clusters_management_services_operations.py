# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.servicefabricmanagedclusters import ServiceFabricManagedClustersManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestServiceFabricManagedClustersManagementServicesOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(ServiceFabricManagedClustersManagementClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_services_get(self, resource_group):
        response = self.client.services.get(
            resource_group_name=resource_group.name,
            cluster_name="str",
            application_name="str",
            service_name="str",
            api_version="2024-09-01-preview",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_services_begin_create_or_update(self, resource_group):
        response = self.client.services.begin_create_or_update(
            resource_group_name=resource_group.name,
            cluster_name="str",
            application_name="str",
            service_name="str",
            parameters={
                "id": "str",
                "location": "str",
                "name": "str",
                "properties": "service_resource_properties",
                "systemData": {
                    "createdAt": "2020-02-20 00:00:00",
                    "createdBy": "str",
                    "createdByType": "str",
                    "lastModifiedAt": "2020-02-20 00:00:00",
                    "lastModifiedBy": "str",
                    "lastModifiedByType": "str",
                },
                "tags": {"str": "str"},
                "type": "str",
            },
            api_version="2024-09-01-preview",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_services_update(self, resource_group):
        response = self.client.services.update(
            resource_group_name=resource_group.name,
            cluster_name="str",
            application_name="str",
            service_name="str",
            parameters={"tags": {"str": "str"}},
            api_version="2024-09-01-preview",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_services_begin_delete(self, resource_group):
        response = self.client.services.begin_delete(
            resource_group_name=resource_group.name,
            cluster_name="str",
            application_name="str",
            service_name="str",
            api_version="2024-09-01-preview",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_services_list_by_applications(self, resource_group):
        response = self.client.services.list_by_applications(
            resource_group_name=resource_group.name,
            cluster_name="str",
            application_name="str",
            api_version="2024-09-01-preview",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...
