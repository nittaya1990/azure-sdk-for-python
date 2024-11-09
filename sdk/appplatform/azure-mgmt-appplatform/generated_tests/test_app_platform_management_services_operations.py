# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.appplatform import AppPlatformManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestAppPlatformManagementServicesOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(AppPlatformManagementClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_get(self, resource_group):
        response = self.client.services.get(
            resource_group_name=resource_group.name,
            service_name="str",
            api_version="2023-12-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_create_or_update(self, resource_group):
        response = self.client.services.begin_create_or_update(
            resource_group_name=resource_group.name,
            service_name="str",
            resource={
                "id": "str",
                "location": "str",
                "name": "str",
                "properties": {
                    "fqdn": "str",
                    "marketplaceResource": {"plan": "str", "product": "str", "publisher": "str"},
                    "networkProfile": {
                        "appNetworkResourceGroup": "str",
                        "appSubnetId": "str",
                        "ingressConfig": {"readTimeoutInSeconds": 0},
                        "outboundIPs": {"publicIPs": ["str"]},
                        "outboundType": "str",
                        "requiredTraffics": [
                            {"direction": "str", "fqdns": ["str"], "ips": ["str"], "port": 0, "protocol": "str"}
                        ],
                        "serviceCidr": "str",
                        "serviceRuntimeNetworkResourceGroup": "str",
                        "serviceRuntimeSubnetId": "str",
                    },
                    "powerState": "str",
                    "provisioningState": "str",
                    "serviceId": "str",
                    "version": 0,
                    "vnetAddons": {"dataPlanePublicEndpoint": False, "logStreamPublicEndpoint": False},
                    "zoneRedundant": False,
                },
                "sku": {"capacity": 0, "name": "S0", "tier": "Standard"},
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
            api_version="2023-12-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_delete(self, resource_group):
        response = self.client.services.begin_delete(
            resource_group_name=resource_group.name,
            service_name="str",
            api_version="2023-12-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_update(self, resource_group):
        response = self.client.services.begin_update(
            resource_group_name=resource_group.name,
            service_name="str",
            resource={
                "id": "str",
                "location": "str",
                "name": "str",
                "properties": {
                    "fqdn": "str",
                    "marketplaceResource": {"plan": "str", "product": "str", "publisher": "str"},
                    "networkProfile": {
                        "appNetworkResourceGroup": "str",
                        "appSubnetId": "str",
                        "ingressConfig": {"readTimeoutInSeconds": 0},
                        "outboundIPs": {"publicIPs": ["str"]},
                        "outboundType": "str",
                        "requiredTraffics": [
                            {"direction": "str", "fqdns": ["str"], "ips": ["str"], "port": 0, "protocol": "str"}
                        ],
                        "serviceCidr": "str",
                        "serviceRuntimeNetworkResourceGroup": "str",
                        "serviceRuntimeSubnetId": "str",
                    },
                    "powerState": "str",
                    "provisioningState": "str",
                    "serviceId": "str",
                    "version": 0,
                    "vnetAddons": {"dataPlanePublicEndpoint": False, "logStreamPublicEndpoint": False},
                    "zoneRedundant": False,
                },
                "sku": {"capacity": 0, "name": "S0", "tier": "Standard"},
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
            api_version="2023-12-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list_test_keys(self, resource_group):
        response = self.client.services.list_test_keys(
            resource_group_name=resource_group.name,
            service_name="str",
            api_version="2023-12-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_regenerate_test_key(self, resource_group):
        response = self.client.services.regenerate_test_key(
            resource_group_name=resource_group.name,
            service_name="str",
            regenerate_test_key_request={"keyType": "str"},
            api_version="2023-12-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_disable_test_endpoint(self, resource_group):
        response = self.client.services.disable_test_endpoint(
            resource_group_name=resource_group.name,
            service_name="str",
            api_version="2023-12-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_enable_test_endpoint(self, resource_group):
        response = self.client.services.enable_test_endpoint(
            resource_group_name=resource_group.name,
            service_name="str",
            api_version="2023-12-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_stop(self, resource_group):
        response = self.client.services.begin_stop(
            resource_group_name=resource_group.name,
            service_name="str",
            api_version="2023-12-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_start(self, resource_group):
        response = self.client.services.begin_start(
            resource_group_name=resource_group.name,
            service_name="str",
            api_version="2023-12-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_flush_vnet_dns_setting(self, resource_group):
        response = self.client.services.begin_flush_vnet_dns_setting(
            resource_group_name=resource_group.name,
            service_name="str",
            api_version="2023-12-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list_supported_apm_types(self, resource_group):
        response = self.client.services.list_supported_apm_types(
            resource_group_name=resource_group.name,
            service_name="str",
            api_version="2023-12-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list_globally_enabled_apms(self, resource_group):
        response = self.client.services.list_globally_enabled_apms(
            resource_group_name=resource_group.name,
            service_name="str",
            api_version="2023-12-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_enable_apm_globally(self, resource_group):
        response = self.client.services.begin_enable_apm_globally(
            resource_group_name=resource_group.name,
            service_name="str",
            apm={"resourceId": "str"},
            api_version="2023-12-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_disable_apm_globally(self, resource_group):
        response = self.client.services.begin_disable_apm_globally(
            resource_group_name=resource_group.name,
            service_name="str",
            apm={"resourceId": "str"},
            api_version="2023-12-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_check_name_availability(self, resource_group):
        response = self.client.services.check_name_availability(
            location="str",
            availability_parameters={"name": "str", "type": "str"},
            api_version="2023-12-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list_by_subscription(self, resource_group):
        response = self.client.services.list_by_subscription(
            api_version="2023-12-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list(self, resource_group):
        response = self.client.services.list(
            resource_group_name=resource_group.name,
            api_version="2023-12-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list_supported_server_versions(self, resource_group):
        response = self.client.services.list_supported_server_versions(
            resource_group_name=resource_group.name,
            service_name="str",
            api_version="2023-12-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...
