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
class TestAppPlatformManagementConfigurationServicesOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(AppPlatformManagementClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_get(self, resource_group):
        response = self.client.configuration_services.get(
            resource_group_name=resource_group.name,
            service_name="str",
            configuration_service_name="str",
            api_version="2023-12-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_create_or_update(self, resource_group):
        response = self.client.configuration_services.begin_create_or_update(
            resource_group_name=resource_group.name,
            service_name="str",
            configuration_service_name="str",
            configuration_service_resource={
                "id": "str",
                "name": "str",
                "properties": {
                    "generation": "Gen1",
                    "instances": [{"name": "str", "status": "str"}],
                    "provisioningState": "str",
                    "resourceRequests": {"cpu": "str", "instanceCount": 0, "memory": "str"},
                    "settings": {
                        "gitProperty": {
                            "repositories": [
                                {
                                    "label": "str",
                                    "name": "str",
                                    "patterns": ["str"],
                                    "uri": "str",
                                    "caCertResourceId": "str",
                                    "gitImplementation": "str",
                                    "hostKey": "str",
                                    "hostKeyAlgorithm": "str",
                                    "password": "str",
                                    "privateKey": "str",
                                    "searchPaths": ["str"],
                                    "strictHostKeyChecking": bool,
                                    "username": "str",
                                }
                            ]
                        }
                    },
                },
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
        response = self.client.configuration_services.begin_delete(
            resource_group_name=resource_group.name,
            service_name="str",
            configuration_service_name="str",
            api_version="2023-12-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list(self, resource_group):
        response = self.client.configuration_services.list(
            resource_group_name=resource_group.name,
            service_name="str",
            api_version="2023-12-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_validate(self, resource_group):
        response = self.client.configuration_services.begin_validate(
            resource_group_name=resource_group.name,
            service_name="str",
            configuration_service_name="str",
            settings={
                "gitProperty": {
                    "repositories": [
                        {
                            "label": "str",
                            "name": "str",
                            "patterns": ["str"],
                            "uri": "str",
                            "caCertResourceId": "str",
                            "gitImplementation": "str",
                            "hostKey": "str",
                            "hostKeyAlgorithm": "str",
                            "password": "str",
                            "privateKey": "str",
                            "searchPaths": ["str"],
                            "strictHostKeyChecking": bool,
                            "username": "str",
                        }
                    ]
                }
            },
            api_version="2023-12-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_validate_resource(self, resource_group):
        response = self.client.configuration_services.begin_validate_resource(
            resource_group_name=resource_group.name,
            service_name="str",
            configuration_service_name="str",
            configuration_service_resource={
                "id": "str",
                "name": "str",
                "properties": {
                    "generation": "Gen1",
                    "instances": [{"name": "str", "status": "str"}],
                    "provisioningState": "str",
                    "resourceRequests": {"cpu": "str", "instanceCount": 0, "memory": "str"},
                    "settings": {
                        "gitProperty": {
                            "repositories": [
                                {
                                    "label": "str",
                                    "name": "str",
                                    "patterns": ["str"],
                                    "uri": "str",
                                    "caCertResourceId": "str",
                                    "gitImplementation": "str",
                                    "hostKey": "str",
                                    "hostKeyAlgorithm": "str",
                                    "password": "str",
                                    "privateKey": "str",
                                    "searchPaths": ["str"],
                                    "strictHostKeyChecking": bool,
                                    "username": "str",
                                }
                            ]
                        }
                    },
                },
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
