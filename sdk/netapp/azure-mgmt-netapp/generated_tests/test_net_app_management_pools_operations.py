# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.netapp import NetAppManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestNetAppManagementPoolsOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(NetAppManagementClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list(self, resource_group):
        response = self.client.pools.list(
            resource_group_name=resource_group.name,
            account_name="str",
            api_version="2024-07-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_get(self, resource_group):
        response = self.client.pools.get(
            resource_group_name=resource_group.name,
            account_name="str",
            pool_name="str",
            api_version="2024-07-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_create_or_update(self, resource_group):
        response = self.client.pools.begin_create_or_update(
            resource_group_name=resource_group.name,
            account_name="str",
            pool_name="str",
            body={
                "location": "str",
                "serviceLevel": "Premium",
                "size": 4398046511104,
                "coolAccess": False,
                "encryptionType": "Single",
                "etag": "str",
                "id": "str",
                "name": "str",
                "poolId": "str",
                "provisioningState": "str",
                "qosType": "str",
                "systemData": {
                    "createdAt": "2020-02-20 00:00:00",
                    "createdBy": "str",
                    "createdByType": "str",
                    "lastModifiedAt": "2020-02-20 00:00:00",
                    "lastModifiedBy": "str",
                    "lastModifiedByType": "str",
                },
                "tags": {"str": "str"},
                "totalThroughputMibps": 0.0,
                "type": "str",
                "utilizedThroughputMibps": 0.0,
            },
            api_version="2024-07-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_update(self, resource_group):
        response = self.client.pools.begin_update(
            resource_group_name=resource_group.name,
            account_name="str",
            pool_name="str",
            body={
                "coolAccess": bool,
                "id": "str",
                "location": "str",
                "name": "str",
                "qosType": "str",
                "size": 4398046511104,
                "tags": {"str": "str"},
                "type": "str",
            },
            api_version="2024-07-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_delete(self, resource_group):
        response = self.client.pools.begin_delete(
            resource_group_name=resource_group.name,
            account_name="str",
            pool_name="str",
            api_version="2024-07-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...
