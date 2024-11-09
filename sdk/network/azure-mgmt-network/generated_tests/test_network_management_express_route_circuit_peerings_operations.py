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
class TestNetworkManagementExpressRouteCircuitPeeringsOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(NetworkManagementClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_delete(self, resource_group):
        response = self.client.express_route_circuit_peerings.begin_delete(
            resource_group_name=resource_group.name,
            circuit_name="str",
            peering_name="str",
            api_version="2024-03-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_get(self, resource_group):
        response = self.client.express_route_circuit_peerings.get(
            resource_group_name=resource_group.name,
            circuit_name="str",
            peering_name="str",
            api_version="2024-03-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_create_or_update(self, resource_group):
        response = self.client.express_route_circuit_peerings.begin_create_or_update(
            resource_group_name=resource_group.name,
            circuit_name="str",
            peering_name="str",
            peering_parameters={
                "azureASN": 0,
                "connections": [
                    {
                        "addressPrefix": "str",
                        "authorizationKey": "str",
                        "circuitConnectionStatus": "str",
                        "etag": "str",
                        "expressRouteCircuitPeering": {"id": "str"},
                        "id": "str",
                        "ipv6CircuitConnectionConfig": {"addressPrefix": "str", "circuitConnectionStatus": "str"},
                        "name": "str",
                        "peerExpressRouteCircuitPeering": {"id": "str"},
                        "provisioningState": "str",
                        "type": "str",
                    }
                ],
                "etag": "str",
                "expressRouteConnection": {"id": "str"},
                "gatewayManagerEtag": "str",
                "id": "str",
                "ipv6PeeringConfig": {
                    "microsoftPeeringConfig": {
                        "advertisedCommunities": ["str"],
                        "advertisedPublicPrefixes": ["str"],
                        "advertisedPublicPrefixesState": "str",
                        "customerASN": 0,
                        "legacyMode": 0,
                        "routingRegistryName": "str",
                    },
                    "primaryPeerAddressPrefix": "str",
                    "routeFilter": {"id": "str"},
                    "secondaryPeerAddressPrefix": "str",
                    "state": "str",
                },
                "lastModifiedBy": "str",
                "microsoftPeeringConfig": {
                    "advertisedCommunities": ["str"],
                    "advertisedPublicPrefixes": ["str"],
                    "advertisedPublicPrefixesState": "str",
                    "customerASN": 0,
                    "legacyMode": 0,
                    "routingRegistryName": "str",
                },
                "name": "str",
                "peerASN": 0,
                "peeredConnections": [
                    {
                        "addressPrefix": "str",
                        "authResourceGuid": "str",
                        "circuitConnectionStatus": "str",
                        "connectionName": "str",
                        "etag": "str",
                        "expressRouteCircuitPeering": {"id": "str"},
                        "id": "str",
                        "name": "str",
                        "peerExpressRouteCircuitPeering": {"id": "str"},
                        "provisioningState": "str",
                        "type": "str",
                    }
                ],
                "peeringType": "str",
                "primaryAzurePort": "str",
                "primaryPeerAddressPrefix": "str",
                "provisioningState": "str",
                "routeFilter": {"id": "str"},
                "secondaryAzurePort": "str",
                "secondaryPeerAddressPrefix": "str",
                "sharedKey": "str",
                "state": "str",
                "stats": {"primarybytesIn": 0, "primarybytesOut": 0, "secondarybytesIn": 0, "secondarybytesOut": 0},
                "type": "str",
                "vlanId": 0,
            },
            api_version="2024-03-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list(self, resource_group):
        response = self.client.express_route_circuit_peerings.list(
            resource_group_name=resource_group.name,
            circuit_name="str",
            api_version="2024-03-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...
