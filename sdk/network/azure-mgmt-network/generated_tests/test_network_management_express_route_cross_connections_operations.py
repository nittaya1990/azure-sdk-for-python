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
class TestNetworkManagementExpressRouteCrossConnectionsOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(NetworkManagementClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list(self, resource_group):
        response = self.client.express_route_cross_connections.list(
            api_version="2024-03-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list_by_resource_group(self, resource_group):
        response = self.client.express_route_cross_connections.list_by_resource_group(
            resource_group_name=resource_group.name,
            api_version="2024-03-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_get(self, resource_group):
        response = self.client.express_route_cross_connections.get(
            resource_group_name=resource_group.name,
            cross_connection_name="str",
            api_version="2024-03-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_create_or_update(self, resource_group):
        response = self.client.express_route_cross_connections.begin_create_or_update(
            resource_group_name=resource_group.name,
            cross_connection_name="str",
            parameters={
                "bandwidthInMbps": 0,
                "etag": "str",
                "expressRouteCircuit": {"id": "str"},
                "id": "str",
                "location": "str",
                "name": "str",
                "peeringLocation": "str",
                "peerings": [
                    {
                        "azureASN": 0,
                        "etag": "str",
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
                        "peeringType": "str",
                        "primaryAzurePort": "str",
                        "primaryPeerAddressPrefix": "str",
                        "provisioningState": "str",
                        "secondaryAzurePort": "str",
                        "secondaryPeerAddressPrefix": "str",
                        "sharedKey": "str",
                        "state": "str",
                        "vlanId": 0,
                    }
                ],
                "primaryAzurePort": "str",
                "provisioningState": "str",
                "sTag": 0,
                "secondaryAzurePort": "str",
                "serviceProviderNotes": "str",
                "serviceProviderProvisioningState": "str",
                "tags": {"str": "str"},
                "type": "str",
            },
            api_version="2024-03-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_update_tags(self, resource_group):
        response = self.client.express_route_cross_connections.update_tags(
            resource_group_name=resource_group.name,
            cross_connection_name="str",
            cross_connection_parameters={"tags": {"str": "str"}},
            api_version="2024-03-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_list_arp_table(self, resource_group):
        response = self.client.express_route_cross_connections.begin_list_arp_table(
            resource_group_name=resource_group.name,
            cross_connection_name="str",
            peering_name="str",
            device_path="str",
            api_version="2024-03-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_list_routes_table_summary(self, resource_group):
        response = self.client.express_route_cross_connections.begin_list_routes_table_summary(
            resource_group_name=resource_group.name,
            cross_connection_name="str",
            peering_name="str",
            device_path="str",
            api_version="2024-03-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_list_routes_table(self, resource_group):
        response = self.client.express_route_cross_connections.begin_list_routes_table(
            resource_group_name=resource_group.name,
            cross_connection_name="str",
            peering_name="str",
            device_path="str",
            api_version="2024-03-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...
