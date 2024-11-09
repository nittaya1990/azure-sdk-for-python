# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.network import NetworkManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestNetworkManagementConnectionMonitorsOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(NetworkManagementClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_create_or_update(self, resource_group):
        response = self.client.connection_monitors.begin_create_or_update(
            resource_group_name=resource_group.name,
            network_watcher_name="str",
            connection_monitor_name="str",
            parameters={
                "autoStart": True,
                "destination": {"address": "str", "port": 0, "resourceId": "str"},
                "endpoints": [
                    {
                        "name": "str",
                        "address": "str",
                        "coverageLevel": "str",
                        "filter": {"items": [{"address": "str", "type": "str"}], "type": "str"},
                        "locationDetails": {"region": "str"},
                        "resourceId": "str",
                        "scope": {"exclude": [{"address": "str"}], "include": [{"address": "str"}]},
                        "subscriptionId": "str",
                        "type": "str",
                    }
                ],
                "location": "str",
                "monitoringIntervalInSeconds": 60,
                "notes": "str",
                "outputs": [{"type": "str", "workspaceSettings": {"workspaceResourceId": "str"}}],
                "source": {"resourceId": "str", "port": 0},
                "tags": {"str": "str"},
                "testConfigurations": [
                    {
                        "name": "str",
                        "protocol": "str",
                        "httpConfiguration": {
                            "method": "str",
                            "path": "str",
                            "port": 0,
                            "preferHTTPS": bool,
                            "requestHeaders": [{"name": "str", "value": "str"}],
                            "validStatusCodeRanges": ["str"],
                        },
                        "icmpConfiguration": {"disableTraceRoute": bool},
                        "preferredIPVersion": "str",
                        "successThreshold": {"checksFailedPercent": 0, "roundTripTimeMs": 0.0},
                        "tcpConfiguration": {"destinationPortBehavior": "str", "disableTraceRoute": bool, "port": 0},
                        "testFrequencySec": 0,
                    }
                ],
                "testGroups": [
                    {
                        "destinations": ["str"],
                        "name": "str",
                        "sources": ["str"],
                        "testConfigurations": ["str"],
                        "disable": bool,
                    }
                ],
            },
            api_version="2024-03-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_get(self, resource_group):
        response = self.client.connection_monitors.get(
            resource_group_name=resource_group.name,
            network_watcher_name="str",
            connection_monitor_name="str",
            api_version="2024-03-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_delete(self, resource_group):
        response = self.client.connection_monitors.begin_delete(
            resource_group_name=resource_group.name,
            network_watcher_name="str",
            connection_monitor_name="str",
            api_version="2024-03-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_update_tags(self, resource_group):
        response = self.client.connection_monitors.update_tags(
            resource_group_name=resource_group.name,
            network_watcher_name="str",
            connection_monitor_name="str",
            parameters={"tags": {"str": "str"}},
            api_version="2024-03-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_stop(self, resource_group):
        response = self.client.connection_monitors.begin_stop(
            resource_group_name=resource_group.name,
            network_watcher_name="str",
            connection_monitor_name="str",
            api_version="2024-03-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_start(self, resource_group):
        response = self.client.connection_monitors.begin_start(
            resource_group_name=resource_group.name,
            network_watcher_name="str",
            connection_monitor_name="str",
            api_version="2024-03-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_query(self, resource_group):
        response = self.client.connection_monitors.begin_query(
            resource_group_name=resource_group.name,
            network_watcher_name="str",
            connection_monitor_name="str",
            api_version="2024-03-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list(self, resource_group):
        response = self.client.connection_monitors.list(
            resource_group_name=resource_group.name,
            network_watcher_name="str",
            api_version="2024-03-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...
