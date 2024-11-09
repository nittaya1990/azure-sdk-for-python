# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.appplatform.aio import AppPlatformManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer
from devtools_testutils.aio import recorded_by_proxy_async

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestAppPlatformManagementBuildServiceOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(AppPlatformManagementClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_list_build_services(self, resource_group):
        response = self.client.build_service.list_build_services(
            resource_group_name=resource_group.name,
            service_name="str",
            api_version="2023-12-01",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_get_build_service(self, resource_group):
        response = await self.client.build_service.get_build_service(
            resource_group_name=resource_group.name,
            service_name="str",
            build_service_name="str",
            api_version="2023-12-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_begin_create_or_update(self, resource_group):
        response = await (
            await self.client.build_service.begin_create_or_update(
                resource_group_name=resource_group.name,
                service_name="str",
                build_service_name="str",
                build_service={
                    "id": "str",
                    "name": "str",
                    "properties": {
                        "containerRegistry": "str",
                        "kPackVersion": "str",
                        "provisioningState": "str",
                        "resourceRequests": {"cpu": "str", "memory": "str"},
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
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_list_builds(self, resource_group):
        response = self.client.build_service.list_builds(
            resource_group_name=resource_group.name,
            service_name="str",
            build_service_name="str",
            api_version="2023-12-01",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_get_build(self, resource_group):
        response = await self.client.build_service.get_build(
            resource_group_name=resource_group.name,
            service_name="str",
            build_service_name="str",
            build_name="str",
            api_version="2023-12-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_create_or_update_build(self, resource_group):
        response = await self.client.build_service.create_or_update_build(
            resource_group_name=resource_group.name,
            service_name="str",
            build_service_name="str",
            build_name="str",
            build={
                "id": "str",
                "name": "str",
                "properties": {
                    "agentPool": "str",
                    "apms": [{"resourceId": "str"}],
                    "builder": "str",
                    "certificates": [{"resourceId": "str"}],
                    "env": {"str": "str"},
                    "provisioningState": "str",
                    "relativePath": "str",
                    "resourceRequests": {"cpu": "1", "memory": "2Gi"},
                    "triggeredBuildResult": {
                        "id": "str",
                        "image": "str",
                        "lastTransitionReason": "str",
                        "lastTransitionStatus": "str",
                        "lastTransitionTime": "2020-02-20 00:00:00",
                        "provisioningState": "str",
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
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_begin_delete_build(self, resource_group):
        response = await (
            await self.client.build_service.begin_delete_build(
                resource_group_name=resource_group.name,
                service_name="str",
                build_service_name="str",
                build_name="str",
                api_version="2023-12-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_list_build_results(self, resource_group):
        response = self.client.build_service.list_build_results(
            resource_group_name=resource_group.name,
            service_name="str",
            build_service_name="str",
            build_name="str",
            api_version="2023-12-01",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_get_build_result(self, resource_group):
        response = await self.client.build_service.get_build_result(
            resource_group_name=resource_group.name,
            service_name="str",
            build_service_name="str",
            build_name="str",
            build_result_name="str",
            api_version="2023-12-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_get_build_result_log(self, resource_group):
        response = await self.client.build_service.get_build_result_log(
            resource_group_name=resource_group.name,
            service_name="str",
            build_service_name="str",
            build_name="str",
            build_result_name="str",
            api_version="2023-12-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_get_resource_upload_url(self, resource_group):
        response = await self.client.build_service.get_resource_upload_url(
            resource_group_name=resource_group.name,
            service_name="str",
            build_service_name="str",
            api_version="2023-12-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_list_supported_buildpacks(self, resource_group):
        response = await self.client.build_service.list_supported_buildpacks(
            resource_group_name=resource_group.name,
            service_name="str",
            build_service_name="str",
            api_version="2023-12-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_get_supported_buildpack(self, resource_group):
        response = await self.client.build_service.get_supported_buildpack(
            resource_group_name=resource_group.name,
            service_name="str",
            build_service_name="str",
            buildpack_name="str",
            api_version="2023-12-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_list_supported_stacks(self, resource_group):
        response = await self.client.build_service.list_supported_stacks(
            resource_group_name=resource_group.name,
            service_name="str",
            build_service_name="str",
            api_version="2023-12-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_get_supported_stack(self, resource_group):
        response = await self.client.build_service.get_supported_stack(
            resource_group_name=resource_group.name,
            service_name="str",
            build_service_name="str",
            stack_name="str",
            api_version="2023-12-01",
        )

        # please add some check logic here by yourself
        # ...
