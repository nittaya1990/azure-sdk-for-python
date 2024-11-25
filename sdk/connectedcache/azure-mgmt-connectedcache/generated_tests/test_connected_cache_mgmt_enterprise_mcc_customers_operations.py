# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.connectedcache import ConnectedCacheMgmtClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestConnectedCacheMgmtEnterpriseMccCustomersOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(ConnectedCacheMgmtClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_enterprise_mcc_customers_get(self, resource_group):
        response = self.client.enterprise_mcc_customers.get(
            resource_group_name=resource_group.name,
            customer_resource_name="str",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_enterprise_mcc_customers_begin_create_or_update(self, resource_group):
        response = self.client.enterprise_mcc_customers.begin_create_or_update(
            resource_group_name=resource_group.name,
            customer_resource_name="str",
            resource={
                "location": "str",
                "id": "str",
                "name": "str",
                "properties": {
                    "additionalCustomerProperties": {
                        "customerAsn": "str",
                        "customerAsnEstimatedEgressPeekGbps": 0.0,
                        "customerEmail": "str",
                        "customerEntitlementExpiration": "2020-02-20 00:00:00",
                        "customerEntitlementSkuGuid": "str",
                        "customerEntitlementSkuId": "str",
                        "customerEntitlementSkuName": "str",
                        "customerOrgName": "str",
                        "customerPropertiesOverviewAverageEgressMbps": 0.0,
                        "customerPropertiesOverviewAverageMissMbps": 0.0,
                        "customerPropertiesOverviewCacheEfficiency": 0.0,
                        "customerPropertiesOverviewCacheNodesHealthyCount": 0,
                        "customerPropertiesOverviewCacheNodesUnhealthyCount": 0,
                        "customerPropertiesOverviewEgressMbpsMax": 0.0,
                        "customerPropertiesOverviewEgressMbpsMaxDateTime": "2020-02-20 00:00:00",
                        "customerPropertiesOverviewMissMbpsMax": 0.0,
                        "customerPropertiesOverviewMissMbpsMaxDateTime": "2020-02-20 00:00:00",
                        "customerTransitAsn": "str",
                        "customerTransitState": "str",
                        "optionalProperty1": "str",
                        "optionalProperty2": "str",
                        "optionalProperty3": "str",
                        "optionalProperty4": "str",
                        "optionalProperty5": "str",
                        "peeringDbLastUpdateDate": "2020-02-20 00:00:00",
                        "peeringDbLastUpdateTime": "2020-02-20 00:00:00",
                        "signupPhaseStatusCode": 0,
                        "signupPhaseStatusText": "str",
                        "signupStatus": bool,
                        "signupStatusCode": 0,
                        "signupStatusText": "str",
                    },
                    "customer": {
                        "clientTenantId": "str",
                        "contactEmail": "str",
                        "contactName": "str",
                        "contactPhone": "str",
                        "createAsyncOperationId": "str",
                        "customerId": "str",
                        "customerName": "str",
                        "deleteAsyncOperationId": "str",
                        "fullyQualifiedResourceId": "str",
                        "isEnterpriseManaged": bool,
                        "isEntitled": bool,
                        "lastSyncWithAzureTimestamp": "2020-02-20 00:00:00",
                        "releaseVersion": 0,
                        "resendSignupCode": bool,
                        "shouldMigrate": bool,
                        "synchWithAzureAttemptsCount": 0,
                        "verifySignupCode": bool,
                        "verifySignupPhrase": "str",
                    },
                    "error": {
                        "additionalInfo": [{"info": {}, "type": "str"}],
                        "code": "str",
                        "details": [...],
                        "message": "str",
                        "target": "str",
                    },
                    "provisioningState": "str",
                    "status": "str",
                    "statusCode": "str",
                    "statusDetails": "str",
                    "statusText": "str",
                },
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
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_enterprise_mcc_customers_update(self, resource_group):
        response = self.client.enterprise_mcc_customers.update(
            resource_group_name=resource_group.name,
            customer_resource_name="str",
            properties={"tags": {"str": "str"}},
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_enterprise_mcc_customers_begin_delete(self, resource_group):
        response = self.client.enterprise_mcc_customers.begin_delete(
            resource_group_name=resource_group.name,
            customer_resource_name="str",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_enterprise_mcc_customers_list_by_resource_group(self, resource_group):
        response = self.client.enterprise_mcc_customers.list_by_resource_group(
            resource_group_name=resource_group.name,
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_enterprise_mcc_customers_list_by_subscription(self, resource_group):
        response = self.client.enterprise_mcc_customers.list_by_subscription()
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...
