# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.devtestlabs import DevTestLabsClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestDevTestLabsCostsOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(DevTestLabsClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_get(self, resource_group):
        response = self.client.costs.get(
            resource_group_name=resource_group.name,
            lab_name="str",
            name="str",
            api_version="2018-09-15",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_create_or_update(self, resource_group):
        response = self.client.costs.create_or_update(
            resource_group_name=resource_group.name,
            lab_name="str",
            name="str",
            lab_cost={
                "createdDate": "2020-02-20 00:00:00",
                "currencyCode": "str",
                "endDateTime": "2020-02-20 00:00:00",
                "id": "str",
                "labCostDetails": [{"cost": 0.0, "costType": "str", "date": "2020-02-20 00:00:00"}],
                "labCostSummary": {"estimatedLabCost": 0.0},
                "location": "str",
                "name": "str",
                "provisioningState": "str",
                "resourceCosts": [
                    {
                        "externalResourceId": "str",
                        "resourceCost": 0.0,
                        "resourceId": "str",
                        "resourceOwner": "str",
                        "resourcePricingTier": "str",
                        "resourceStatus": "str",
                        "resourceType": "str",
                        "resourceUId": "str",
                        "resourcename": "str",
                    }
                ],
                "startDateTime": "2020-02-20 00:00:00",
                "tags": {"str": "str"},
                "targetCost": {
                    "costThresholds": [
                        {
                            "displayOnChart": "str",
                            "notificationSent": "str",
                            "percentageThreshold": {"thresholdValue": 0.0},
                            "sendNotificationWhenExceeded": "str",
                            "thresholdId": "str",
                        }
                    ],
                    "cycleEndDateTime": "2020-02-20 00:00:00",
                    "cycleStartDateTime": "2020-02-20 00:00:00",
                    "cycleType": "str",
                    "status": "str",
                    "target": 0,
                },
                "type": "str",
                "uniqueIdentifier": "str",
            },
            api_version="2018-09-15",
        )

        # please add some check logic here by yourself
        # ...
