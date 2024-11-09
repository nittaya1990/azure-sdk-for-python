# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.sql.aio import SqlManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer
from devtools_testutils.aio import recorded_by_proxy_async

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestSqlManagementManagedInstanceDtcsOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(SqlManagementClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_list_by_managed_instance(self, resource_group):
        response = self.client.managed_instance_dtcs.list_by_managed_instance(
            resource_group_name=resource_group.name,
            managed_instance_name="str",
            api_version="2022-05-01-preview",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_get(self, resource_group):
        response = await self.client.managed_instance_dtcs.get(
            resource_group_name=resource_group.name,
            managed_instance_name="str",
            dtc_name="str",
            api_version="2022-05-01-preview",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_begin_create_or_update(self, resource_group):
        response = await (
            await self.client.managed_instance_dtcs.begin_create_or_update(
                resource_group_name=resource_group.name,
                managed_instance_name="str",
                dtc_name="str",
                parameters={
                    "dtcEnabled": bool,
                    "dtcHostNameDnsSuffix": "str",
                    "externalDnsSuffixSearchList": ["str"],
                    "id": "str",
                    "name": "str",
                    "provisioningState": "str",
                    "securitySettings": {
                        "snaLu6point2TransactionsEnabled": bool,
                        "transactionManagerCommunicationSettings": {
                            "allowInboundEnabled": bool,
                            "allowOutboundEnabled": bool,
                            "authentication": "str",
                        },
                        "xaTransactionsDefaultTimeout": 0,
                        "xaTransactionsEnabled": bool,
                        "xaTransactionsMaximumTimeout": 0,
                    },
                    "type": "str",
                },
                api_version="2022-05-01-preview",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...
