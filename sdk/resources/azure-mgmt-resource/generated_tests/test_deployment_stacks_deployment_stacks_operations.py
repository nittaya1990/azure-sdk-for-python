# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.resource import DeploymentStacksClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestDeploymentStacksDeploymentStacksOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(DeploymentStacksClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list_at_resource_group(self, resource_group):
        response = self.client.deployment_stacks.list_at_resource_group(
            resource_group_name=resource_group.name,
            api_version="2022-08-01-preview",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list_at_subscription(self, resource_group):
        response = self.client.deployment_stacks.list_at_subscription(
            api_version="2022-08-01-preview",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list_at_management_group(self, resource_group):
        response = self.client.deployment_stacks.list_at_management_group(
            management_group_id="str",
            api_version="2022-08-01-preview",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_create_or_update_at_resource_group(self, resource_group):
        response = self.client.deployment_stacks.begin_create_or_update_at_resource_group(
            resource_group_name=resource_group.name,
            deployment_stack_name="str",
            deployment_stack={
                "actionOnUnmanage": {"resources": "str", "managementGroups": "str", "resourceGroups": "str"},
                "debugSetting": {"detailLevel": "str"},
                "deletedResources": [{"id": "str"}],
                "denySettings": {
                    "mode": "str",
                    "applyToChildScopes": bool,
                    "excludedActions": ["str"],
                    "excludedPrincipals": ["str"],
                },
                "deploymentId": "str",
                "deploymentScope": "str",
                "description": "str",
                "detachedResources": [{"id": "str"}],
                "duration": "str",
                "error": {
                    "error": {
                        "additionalInfo": [{"info": {}, "type": "str"}],
                        "code": "str",
                        "details": [...],
                        "message": "str",
                        "target": "str",
                    }
                },
                "failedResources": [
                    {
                        "error": {
                            "error": {
                                "additionalInfo": [{"info": {}, "type": "str"}],
                                "code": "str",
                                "details": [...],
                                "message": "str",
                                "target": "str",
                            }
                        },
                        "id": "str",
                    }
                ],
                "id": "str",
                "location": "str",
                "name": "str",
                "outputs": {},
                "parameters": {},
                "parametersLink": {"uri": "str", "contentVersion": "str"},
                "provisioningState": "str",
                "resources": [{"denyStatus": "None", "id": "str", "status": "None"}],
                "systemData": {
                    "createdAt": "2020-02-20 00:00:00",
                    "createdBy": "str",
                    "createdByType": "str",
                    "lastModifiedAt": "2020-02-20 00:00:00",
                    "lastModifiedBy": "str",
                    "lastModifiedByType": "str",
                },
                "tags": {"str": "str"},
                "template": {},
                "templateLink": {
                    "contentVersion": "str",
                    "id": "str",
                    "queryString": "str",
                    "relativePath": "str",
                    "uri": "str",
                },
                "type": "str",
            },
            api_version="2022-08-01-preview",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_get_at_resource_group(self, resource_group):
        response = self.client.deployment_stacks.get_at_resource_group(
            resource_group_name=resource_group.name,
            deployment_stack_name="str",
            api_version="2022-08-01-preview",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_delete_at_resource_group(self, resource_group):
        response = self.client.deployment_stacks.begin_delete_at_resource_group(
            resource_group_name=resource_group.name,
            deployment_stack_name="str",
            api_version="2022-08-01-preview",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_create_or_update_at_subscription(self, resource_group):
        response = self.client.deployment_stacks.begin_create_or_update_at_subscription(
            deployment_stack_name="str",
            deployment_stack={
                "actionOnUnmanage": {"resources": "str", "managementGroups": "str", "resourceGroups": "str"},
                "debugSetting": {"detailLevel": "str"},
                "deletedResources": [{"id": "str"}],
                "denySettings": {
                    "mode": "str",
                    "applyToChildScopes": bool,
                    "excludedActions": ["str"],
                    "excludedPrincipals": ["str"],
                },
                "deploymentId": "str",
                "deploymentScope": "str",
                "description": "str",
                "detachedResources": [{"id": "str"}],
                "duration": "str",
                "error": {
                    "error": {
                        "additionalInfo": [{"info": {}, "type": "str"}],
                        "code": "str",
                        "details": [...],
                        "message": "str",
                        "target": "str",
                    }
                },
                "failedResources": [
                    {
                        "error": {
                            "error": {
                                "additionalInfo": [{"info": {}, "type": "str"}],
                                "code": "str",
                                "details": [...],
                                "message": "str",
                                "target": "str",
                            }
                        },
                        "id": "str",
                    }
                ],
                "id": "str",
                "location": "str",
                "name": "str",
                "outputs": {},
                "parameters": {},
                "parametersLink": {"uri": "str", "contentVersion": "str"},
                "provisioningState": "str",
                "resources": [{"denyStatus": "None", "id": "str", "status": "None"}],
                "systemData": {
                    "createdAt": "2020-02-20 00:00:00",
                    "createdBy": "str",
                    "createdByType": "str",
                    "lastModifiedAt": "2020-02-20 00:00:00",
                    "lastModifiedBy": "str",
                    "lastModifiedByType": "str",
                },
                "tags": {"str": "str"},
                "template": {},
                "templateLink": {
                    "contentVersion": "str",
                    "id": "str",
                    "queryString": "str",
                    "relativePath": "str",
                    "uri": "str",
                },
                "type": "str",
            },
            api_version="2022-08-01-preview",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_get_at_subscription(self, resource_group):
        response = self.client.deployment_stacks.get_at_subscription(
            deployment_stack_name="str",
            api_version="2022-08-01-preview",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_delete_at_subscription(self, resource_group):
        response = self.client.deployment_stacks.begin_delete_at_subscription(
            deployment_stack_name="str",
            api_version="2022-08-01-preview",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_create_or_update_at_management_group(self, resource_group):
        response = self.client.deployment_stacks.begin_create_or_update_at_management_group(
            management_group_id="str",
            deployment_stack_name="str",
            deployment_stack={
                "actionOnUnmanage": {"resources": "str", "managementGroups": "str", "resourceGroups": "str"},
                "debugSetting": {"detailLevel": "str"},
                "deletedResources": [{"id": "str"}],
                "denySettings": {
                    "mode": "str",
                    "applyToChildScopes": bool,
                    "excludedActions": ["str"],
                    "excludedPrincipals": ["str"],
                },
                "deploymentId": "str",
                "deploymentScope": "str",
                "description": "str",
                "detachedResources": [{"id": "str"}],
                "duration": "str",
                "error": {
                    "error": {
                        "additionalInfo": [{"info": {}, "type": "str"}],
                        "code": "str",
                        "details": [...],
                        "message": "str",
                        "target": "str",
                    }
                },
                "failedResources": [
                    {
                        "error": {
                            "error": {
                                "additionalInfo": [{"info": {}, "type": "str"}],
                                "code": "str",
                                "details": [...],
                                "message": "str",
                                "target": "str",
                            }
                        },
                        "id": "str",
                    }
                ],
                "id": "str",
                "location": "str",
                "name": "str",
                "outputs": {},
                "parameters": {},
                "parametersLink": {"uri": "str", "contentVersion": "str"},
                "provisioningState": "str",
                "resources": [{"denyStatus": "None", "id": "str", "status": "None"}],
                "systemData": {
                    "createdAt": "2020-02-20 00:00:00",
                    "createdBy": "str",
                    "createdByType": "str",
                    "lastModifiedAt": "2020-02-20 00:00:00",
                    "lastModifiedBy": "str",
                    "lastModifiedByType": "str",
                },
                "tags": {"str": "str"},
                "template": {},
                "templateLink": {
                    "contentVersion": "str",
                    "id": "str",
                    "queryString": "str",
                    "relativePath": "str",
                    "uri": "str",
                },
                "type": "str",
            },
            api_version="2022-08-01-preview",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_get_at_management_group(self, resource_group):
        response = self.client.deployment_stacks.get_at_management_group(
            management_group_id="str",
            deployment_stack_name="str",
            api_version="2022-08-01-preview",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_delete_at_management_group(self, resource_group):
        response = self.client.deployment_stacks.begin_delete_at_management_group(
            management_group_id="str",
            deployment_stack_name="str",
            api_version="2022-08-01-preview",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_export_template_at_resource_group(self, resource_group):
        response = self.client.deployment_stacks.export_template_at_resource_group(
            resource_group_name=resource_group.name,
            deployment_stack_name="str",
            api_version="2022-08-01-preview",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_export_template_at_subscription(self, resource_group):
        response = self.client.deployment_stacks.export_template_at_subscription(
            deployment_stack_name="str",
            api_version="2022-08-01-preview",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_export_template_at_management_group(self, resource_group):
        response = self.client.deployment_stacks.export_template_at_management_group(
            management_group_id="str",
            deployment_stack_name="str",
            api_version="2022-08-01-preview",
        )

        # please add some check logic here by yourself
        # ...
