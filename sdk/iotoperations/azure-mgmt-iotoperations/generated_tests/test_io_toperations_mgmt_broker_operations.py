# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.iotoperations import IoTOperationsMgmtClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestIoTOperationsMgmtBrokerOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(IoTOperationsMgmtClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_broker_get(self, resource_group):
        response = self.client.broker.get(
            resource_group_name=resource_group.name,
            instance_name="str",
            broker_name="str",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_broker_begin_create_or_update(self, resource_group):
        response = self.client.broker.begin_create_or_update(
            resource_group_name=resource_group.name,
            instance_name="str",
            broker_name="str",
            resource={
                "extendedLocation": {"name": "str", "type": "str"},
                "id": "str",
                "name": "str",
                "properties": {
                    "advanced": {
                        "clients": {
                            "maxKeepAliveSeconds": 0,
                            "maxMessageExpirySeconds": 0,
                            "maxPacketSizeBytes": 0,
                            "maxReceiveMaximum": 0,
                            "maxSessionExpirySeconds": 0,
                            "subscriberQueueLimit": {"length": 0, "strategy": "str"},
                        },
                        "encryptInternalTraffic": "str",
                        "internalCerts": {
                            "duration": "str",
                            "privateKey": {"algorithm": "str", "rotationPolicy": "str"},
                            "renewBefore": "str",
                        },
                    },
                    "cardinality": {
                        "backendChain": {"partitions": 0, "redundancyFactor": 0, "workers": 0},
                        "frontend": {"replicas": 0, "workers": 0},
                    },
                    "diagnostics": {
                        "logs": {"level": "str"},
                        "metrics": {"prometheusPort": 0},
                        "selfCheck": {"intervalSeconds": 0, "mode": "str", "timeoutSeconds": 0},
                        "traces": {
                            "cacheSizeMegabytes": 0,
                            "mode": "str",
                            "selfTracing": {"intervalSeconds": 0, "mode": "str"},
                            "spanChannelCapacity": 0,
                        },
                    },
                    "diskBackedMessageBuffer": {
                        "maxSize": "str",
                        "ephemeralVolumeClaimSpec": {
                            "accessModes": ["str"],
                            "dataSource": {"kind": "str", "name": "str", "apiGroup": "str"},
                            "dataSourceRef": {"kind": "str", "name": "str", "apiGroup": "str", "namespace": "str"},
                            "resources": {"limits": {"str": "str"}, "requests": {"str": "str"}},
                            "selector": {
                                "matchExpressions": [{"key": "str", "operator": "str", "values": ["str"]}],
                                "matchLabels": {"str": "str"},
                            },
                            "storageClassName": "str",
                            "volumeMode": "str",
                            "volumeName": "str",
                        },
                        "persistentVolumeClaimSpec": {
                            "accessModes": ["str"],
                            "dataSource": {"kind": "str", "name": "str", "apiGroup": "str"},
                            "dataSourceRef": {"kind": "str", "name": "str", "apiGroup": "str", "namespace": "str"},
                            "resources": {"limits": {"str": "str"}, "requests": {"str": "str"}},
                            "selector": {
                                "matchExpressions": [{"key": "str", "operator": "str", "values": ["str"]}],
                                "matchLabels": {"str": "str"},
                            },
                            "storageClassName": "str",
                            "volumeMode": "str",
                            "volumeName": "str",
                        },
                    },
                    "generateResourceLimits": {"cpu": "str"},
                    "memoryProfile": "str",
                    "provisioningState": "str",
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
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_broker_begin_delete(self, resource_group):
        response = self.client.broker.begin_delete(
            resource_group_name=resource_group.name,
            instance_name="str",
            broker_name="str",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_broker_list_by_resource_group(self, resource_group):
        response = self.client.broker.list_by_resource_group(
            resource_group_name=resource_group.name,
            instance_name="str",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...
