# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import datetime
from typing import Any, Dict, List, Optional, TYPE_CHECKING, Union

from .. import _serialization

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from .. import models as _models


class ErrorAdditionalInfo(_serialization.Model):
    """The resource management error additional info.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar type: The additional info type.
    :vartype type: str
    :ivar info: The additional info.
    :vartype info: JSON
    """

    _validation = {
        "type": {"readonly": True},
        "info": {"readonly": True},
    }

    _attribute_map = {
        "type": {"key": "type", "type": "str"},
        "info": {"key": "info", "type": "object"},
    }

    def __init__(self, **kwargs: Any) -> None:
        """ """
        super().__init__(**kwargs)
        self.type = None
        self.info = None


class ErrorDetail(_serialization.Model):
    """The error detail.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar code: The error code.
    :vartype code: str
    :ivar message: The error message.
    :vartype message: str
    :ivar target: The error target.
    :vartype target: str
    :ivar details: The error details.
    :vartype details: list[~azure.mgmt.qumulo.models.ErrorDetail]
    :ivar additional_info: The error additional info.
    :vartype additional_info: list[~azure.mgmt.qumulo.models.ErrorAdditionalInfo]
    """

    _validation = {
        "code": {"readonly": True},
        "message": {"readonly": True},
        "target": {"readonly": True},
        "details": {"readonly": True},
        "additional_info": {"readonly": True},
    }

    _attribute_map = {
        "code": {"key": "code", "type": "str"},
        "message": {"key": "message", "type": "str"},
        "target": {"key": "target", "type": "str"},
        "details": {"key": "details", "type": "[ErrorDetail]"},
        "additional_info": {"key": "additionalInfo", "type": "[ErrorAdditionalInfo]"},
    }

    def __init__(self, **kwargs: Any) -> None:
        """ """
        super().__init__(**kwargs)
        self.code = None
        self.message = None
        self.target = None
        self.details = None
        self.additional_info = None


class ErrorResponse(_serialization.Model):
    """Common error response for all Azure Resource Manager APIs to return error details for failed
    operations. (This also follows the OData error response format.).

    :ivar error: The error object.
    :vartype error: ~azure.mgmt.qumulo.models.ErrorDetail
    """

    _attribute_map = {
        "error": {"key": "error", "type": "ErrorDetail"},
    }

    def __init__(self, *, error: Optional["_models.ErrorDetail"] = None, **kwargs: Any) -> None:
        """
        :keyword error: The error object.
        :paramtype error: ~azure.mgmt.qumulo.models.ErrorDetail
        """
        super().__init__(**kwargs)
        self.error = error


class Resource(_serialization.Model):
    """Common fields that are returned in the response for all Azure Resource Manager resources.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.  # pylint: disable=line-too-long
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :ivar system_data: Azure Resource Manager metadata containing createdBy and modifiedBy
     information.
    :vartype system_data: ~azure.mgmt.qumulo.models.SystemData
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
        "system_data": {"readonly": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "system_data": {"key": "systemData", "type": "SystemData"},
    }

    def __init__(self, **kwargs: Any) -> None:
        """ """
        super().__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.system_data = None


class TrackedResource(Resource):
    """The resource model definition for an Azure Resource Manager tracked top level resource which
    has 'tags' and a 'location'.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to server.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.  # pylint: disable=line-too-long
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :ivar system_data: Azure Resource Manager metadata containing createdBy and modifiedBy
     information.
    :vartype system_data: ~azure.mgmt.qumulo.models.SystemData
    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    :ivar location: The geo-location where the resource lives. Required.
    :vartype location: str
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
        "system_data": {"readonly": True},
        "location": {"required": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "system_data": {"key": "systemData", "type": "SystemData"},
        "tags": {"key": "tags", "type": "{str}"},
        "location": {"key": "location", "type": "str"},
    }

    def __init__(self, *, location: str, tags: Optional[Dict[str, str]] = None, **kwargs: Any) -> None:
        """
        :keyword tags: Resource tags.
        :paramtype tags: dict[str, str]
        :keyword location: The geo-location where the resource lives. Required.
        :paramtype location: str
        """
        super().__init__(**kwargs)
        self.tags = tags
        self.location = location


class FileSystemResource(TrackedResource):  # pylint: disable=too-many-instance-attributes
    """Concrete tracked resource types can be created by aliasing this type using a specific property
    type.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to server.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.  # pylint: disable=line-too-long
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :ivar system_data: Azure Resource Manager metadata containing createdBy and modifiedBy
     information.
    :vartype system_data: ~azure.mgmt.qumulo.models.SystemData
    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    :ivar location: The geo-location where the resource lives. Required.
    :vartype location: str
    :ivar identity: The managed service identities assigned to this resource.
    :vartype identity: ~azure.mgmt.qumulo.models.ManagedServiceIdentity
    :ivar marketplace_details: Marketplace details.
    :vartype marketplace_details: ~azure.mgmt.qumulo.models.MarketplaceDetails
    :ivar provisioning_state: Provisioning State of the resource. Known values are: "Accepted",
     "Creating", "Updating", "Deleting", "Succeeded", "Failed", "Canceled", and "Deleted".
    :vartype provisioning_state: str or ~azure.mgmt.qumulo.models.ProvisioningState
    :ivar storage_sku: Storage Sku.
    :vartype storage_sku: str
    :ivar user_details: User Details.
    :vartype user_details: ~azure.mgmt.qumulo.models.UserDetails
    :ivar delegated_subnet_id: Delegated subnet id for Vnet injection.
    :vartype delegated_subnet_id: str
    :ivar cluster_login_url: File system Id of the resource.
    :vartype cluster_login_url: str
    :ivar private_ips: Private IPs of the resource.
    :vartype private_ips: list[str]
    :ivar admin_password: Initial administrator password of the resource.
    :vartype admin_password: str
    :ivar availability_zone: Availability zone.
    :vartype availability_zone: str
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
        "system_data": {"readonly": True},
        "location": {"required": True},
        "provisioning_state": {"readonly": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "system_data": {"key": "systemData", "type": "SystemData"},
        "tags": {"key": "tags", "type": "{str}"},
        "location": {"key": "location", "type": "str"},
        "identity": {"key": "identity", "type": "ManagedServiceIdentity"},
        "marketplace_details": {"key": "properties.marketplaceDetails", "type": "MarketplaceDetails"},
        "provisioning_state": {"key": "properties.provisioningState", "type": "str"},
        "storage_sku": {"key": "properties.storageSku", "type": "str"},
        "user_details": {"key": "properties.userDetails", "type": "UserDetails"},
        "delegated_subnet_id": {"key": "properties.delegatedSubnetId", "type": "str"},
        "cluster_login_url": {"key": "properties.clusterLoginUrl", "type": "str"},
        "private_ips": {"key": "properties.privateIPs", "type": "[str]"},
        "admin_password": {"key": "properties.adminPassword", "type": "str"},
        "availability_zone": {"key": "properties.availabilityZone", "type": "str"},
    }

    def __init__(
        self,
        *,
        location: str,
        tags: Optional[Dict[str, str]] = None,
        identity: Optional["_models.ManagedServiceIdentity"] = None,
        marketplace_details: Optional["_models.MarketplaceDetails"] = None,
        storage_sku: Optional[str] = None,
        user_details: Optional["_models.UserDetails"] = None,
        delegated_subnet_id: Optional[str] = None,
        cluster_login_url: Optional[str] = None,
        private_ips: Optional[List[str]] = None,
        admin_password: Optional[str] = None,
        availability_zone: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword tags: Resource tags.
        :paramtype tags: dict[str, str]
        :keyword location: The geo-location where the resource lives. Required.
        :paramtype location: str
        :keyword identity: The managed service identities assigned to this resource.
        :paramtype identity: ~azure.mgmt.qumulo.models.ManagedServiceIdentity
        :keyword marketplace_details: Marketplace details.
        :paramtype marketplace_details: ~azure.mgmt.qumulo.models.MarketplaceDetails
        :keyword storage_sku: Storage Sku.
        :paramtype storage_sku: str
        :keyword user_details: User Details.
        :paramtype user_details: ~azure.mgmt.qumulo.models.UserDetails
        :keyword delegated_subnet_id: Delegated subnet id for Vnet injection.
        :paramtype delegated_subnet_id: str
        :keyword cluster_login_url: File system Id of the resource.
        :paramtype cluster_login_url: str
        :keyword private_ips: Private IPs of the resource.
        :paramtype private_ips: list[str]
        :keyword admin_password: Initial administrator password of the resource.
        :paramtype admin_password: str
        :keyword availability_zone: Availability zone.
        :paramtype availability_zone: str
        """
        super().__init__(tags=tags, location=location, **kwargs)
        self.identity = identity
        self.marketplace_details = marketplace_details
        self.provisioning_state = None
        self.storage_sku = storage_sku
        self.user_details = user_details
        self.delegated_subnet_id = delegated_subnet_id
        self.cluster_login_url = cluster_login_url
        self.private_ips = private_ips
        self.admin_password = admin_password
        self.availability_zone = availability_zone


class FileSystemResourceListResult(_serialization.Model):
    """The response of a FileSystemResource list operation.

    All required parameters must be populated in order to send to server.

    :ivar value: The FileSystemResource items on this page. Required.
    :vartype value: list[~azure.mgmt.qumulo.models.FileSystemResource]
    :ivar next_link: The link to the next page of items.
    :vartype next_link: str
    """

    _validation = {
        "value": {"required": True},
    }

    _attribute_map = {
        "value": {"key": "value", "type": "[FileSystemResource]"},
        "next_link": {"key": "nextLink", "type": "str"},
    }

    def __init__(
        self, *, value: List["_models.FileSystemResource"], next_link: Optional[str] = None, **kwargs: Any
    ) -> None:
        """
        :keyword value: The FileSystemResource items on this page. Required.
        :paramtype value: list[~azure.mgmt.qumulo.models.FileSystemResource]
        :keyword next_link: The link to the next page of items.
        :paramtype next_link: str
        """
        super().__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class FileSystemResourceUpdate(_serialization.Model):
    """The type used for update operations of the FileSystemResource.

    :ivar identity: The managed service identities assigned to this resource.
    :vartype identity: ~azure.mgmt.qumulo.models.ManagedServiceIdentity
    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    :ivar properties: The updatable properties of the FileSystemResource.
    :vartype properties: ~azure.mgmt.qumulo.models.FileSystemResourceUpdateProperties
    """

    _attribute_map = {
        "identity": {"key": "identity", "type": "ManagedServiceIdentity"},
        "tags": {"key": "tags", "type": "{str}"},
        "properties": {"key": "properties", "type": "FileSystemResourceUpdateProperties"},
    }

    def __init__(
        self,
        *,
        identity: Optional["_models.ManagedServiceIdentity"] = None,
        tags: Optional[Dict[str, str]] = None,
        properties: Optional["_models.FileSystemResourceUpdateProperties"] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword identity: The managed service identities assigned to this resource.
        :paramtype identity: ~azure.mgmt.qumulo.models.ManagedServiceIdentity
        :keyword tags: Resource tags.
        :paramtype tags: dict[str, str]
        :keyword properties: The updatable properties of the FileSystemResource.
        :paramtype properties: ~azure.mgmt.qumulo.models.FileSystemResourceUpdateProperties
        """
        super().__init__(**kwargs)
        self.identity = identity
        self.tags = tags
        self.properties = properties


class FileSystemResourceUpdateProperties(_serialization.Model):
    """The updatable properties of the FileSystemResource.

    :ivar marketplace_details: Marketplace details.
    :vartype marketplace_details: ~azure.mgmt.qumulo.models.MarketplaceDetails
    :ivar user_details: User Details.
    :vartype user_details: ~azure.mgmt.qumulo.models.UserDetails
    :ivar delegated_subnet_id: Delegated subnet id for Vnet injection.
    :vartype delegated_subnet_id: str
    """

    _attribute_map = {
        "marketplace_details": {"key": "marketplaceDetails", "type": "MarketplaceDetails"},
        "user_details": {"key": "userDetails", "type": "UserDetails"},
        "delegated_subnet_id": {"key": "delegatedSubnetId", "type": "str"},
    }

    def __init__(
        self,
        *,
        marketplace_details: Optional["_models.MarketplaceDetails"] = None,
        user_details: Optional["_models.UserDetails"] = None,
        delegated_subnet_id: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword marketplace_details: Marketplace details.
        :paramtype marketplace_details: ~azure.mgmt.qumulo.models.MarketplaceDetails
        :keyword user_details: User Details.
        :paramtype user_details: ~azure.mgmt.qumulo.models.UserDetails
        :keyword delegated_subnet_id: Delegated subnet id for Vnet injection.
        :paramtype delegated_subnet_id: str
        """
        super().__init__(**kwargs)
        self.marketplace_details = marketplace_details
        self.user_details = user_details
        self.delegated_subnet_id = delegated_subnet_id


class ManagedServiceIdentity(_serialization.Model):
    """Managed service identity (system assigned and/or user assigned identities).

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to server.

    :ivar principal_id: The service principal ID of the system assigned identity. This property
     will only be provided for a system assigned identity.
    :vartype principal_id: str
    :ivar tenant_id: The tenant ID of the system assigned identity. This property will only be
     provided for a system assigned identity.
    :vartype tenant_id: str
    :ivar type: Type of managed service identity (where both SystemAssigned and UserAssigned types
     are allowed). Required. Known values are: "None", "SystemAssigned", "UserAssigned", and
     "SystemAssigned,UserAssigned".
    :vartype type: str or ~azure.mgmt.qumulo.models.ManagedServiceIdentityType
    :ivar user_assigned_identities: The set of user assigned identities associated with the
     resource. The userAssignedIdentities dictionary keys will be ARM resource ids in the form:
     '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}.  # pylint: disable=line-too-long
     The dictionary values can be empty objects ({}) in requests.
    :vartype user_assigned_identities: dict[str, ~azure.mgmt.qumulo.models.UserAssignedIdentity]
    """

    _validation = {
        "principal_id": {"readonly": True},
        "tenant_id": {"readonly": True},
        "type": {"required": True},
    }

    _attribute_map = {
        "principal_id": {"key": "principalId", "type": "str"},
        "tenant_id": {"key": "tenantId", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "user_assigned_identities": {"key": "userAssignedIdentities", "type": "{UserAssignedIdentity}"},
    }

    def __init__(
        self,
        *,
        type: Union[str, "_models.ManagedServiceIdentityType"],
        user_assigned_identities: Optional[Dict[str, "_models.UserAssignedIdentity"]] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword type: Type of managed service identity (where both SystemAssigned and UserAssigned
         types are allowed). Required. Known values are: "None", "SystemAssigned", "UserAssigned", and
         "SystemAssigned,UserAssigned".
        :paramtype type: str or ~azure.mgmt.qumulo.models.ManagedServiceIdentityType
        :keyword user_assigned_identities: The set of user assigned identities associated with the
         resource. The userAssignedIdentities dictionary keys will be ARM resource ids in the form:
         '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}.  # pylint: disable=line-too-long
         The dictionary values can be empty objects ({}) in requests.
        :paramtype user_assigned_identities: dict[str, ~azure.mgmt.qumulo.models.UserAssignedIdentity]
        """
        super().__init__(**kwargs)
        self.principal_id = None
        self.tenant_id = None
        self.type = type
        self.user_assigned_identities = user_assigned_identities


class MarketplaceDetails(_serialization.Model):
    """MarketplaceDetails of Qumulo FileSystem resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to server.

    :ivar marketplace_subscription_id: Marketplace Subscription Id.
    :vartype marketplace_subscription_id: str
    :ivar plan_id: Plan Id. Required.
    :vartype plan_id: str
    :ivar offer_id: Offer Id. Required.
    :vartype offer_id: str
    :ivar publisher_id: Publisher Id.
    :vartype publisher_id: str
    :ivar term_unit: Term Unit.
    :vartype term_unit: str
    :ivar marketplace_subscription_status: Marketplace subscription status. Known values are:
     "PendingFulfillmentStart", "Subscribed", "Suspended", and "Unsubscribed".
    :vartype marketplace_subscription_status: str or
     ~azure.mgmt.qumulo.models.MarketplaceSubscriptionStatus
    """

    _validation = {
        "plan_id": {"required": True},
        "offer_id": {"required": True},
        "marketplace_subscription_status": {"readonly": True},
    }

    _attribute_map = {
        "marketplace_subscription_id": {"key": "marketplaceSubscriptionId", "type": "str"},
        "plan_id": {"key": "planId", "type": "str"},
        "offer_id": {"key": "offerId", "type": "str"},
        "publisher_id": {"key": "publisherId", "type": "str"},
        "term_unit": {"key": "termUnit", "type": "str"},
        "marketplace_subscription_status": {"key": "marketplaceSubscriptionStatus", "type": "str"},
    }

    def __init__(
        self,
        *,
        plan_id: str,
        offer_id: str,
        marketplace_subscription_id: Optional[str] = None,
        publisher_id: Optional[str] = None,
        term_unit: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword marketplace_subscription_id: Marketplace Subscription Id.
        :paramtype marketplace_subscription_id: str
        :keyword plan_id: Plan Id. Required.
        :paramtype plan_id: str
        :keyword offer_id: Offer Id. Required.
        :paramtype offer_id: str
        :keyword publisher_id: Publisher Id.
        :paramtype publisher_id: str
        :keyword term_unit: Term Unit.
        :paramtype term_unit: str
        """
        super().__init__(**kwargs)
        self.marketplace_subscription_id = marketplace_subscription_id
        self.plan_id = plan_id
        self.offer_id = offer_id
        self.publisher_id = publisher_id
        self.term_unit = term_unit
        self.marketplace_subscription_status = None


class Operation(_serialization.Model):
    """Details of a REST API operation, returned from the Resource Provider Operations API.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar name: The name of the operation, as per Resource-Based Access Control (RBAC). Examples:
     "Microsoft.Compute/virtualMachines/write", "Microsoft.Compute/virtualMachines/capture/action".
    :vartype name: str
    :ivar is_data_action: Whether the operation applies to data-plane. This is "true" for
     data-plane operations and "false" for ARM/control-plane operations.
    :vartype is_data_action: bool
    :ivar display: Localized display information for this particular operation.
    :vartype display: ~azure.mgmt.qumulo.models.OperationDisplay
    :ivar origin: The intended executor of the operation; as in Resource Based Access Control
     (RBAC) and audit logs UX. Default value is "user,system". Known values are: "user", "system",
     and "user,system".
    :vartype origin: str or ~azure.mgmt.qumulo.models.Origin
    :ivar action_type: Enum. Indicates the action type. "Internal" refers to actions that are for
     internal only APIs. "Internal"
    :vartype action_type: str or ~azure.mgmt.qumulo.models.ActionType
    """

    _validation = {
        "name": {"readonly": True},
        "is_data_action": {"readonly": True},
        "origin": {"readonly": True},
        "action_type": {"readonly": True},
    }

    _attribute_map = {
        "name": {"key": "name", "type": "str"},
        "is_data_action": {"key": "isDataAction", "type": "bool"},
        "display": {"key": "display", "type": "OperationDisplay"},
        "origin": {"key": "origin", "type": "str"},
        "action_type": {"key": "actionType", "type": "str"},
    }

    def __init__(self, *, display: Optional["_models.OperationDisplay"] = None, **kwargs: Any) -> None:
        """
        :keyword display: Localized display information for this particular operation.
        :paramtype display: ~azure.mgmt.qumulo.models.OperationDisplay
        """
        super().__init__(**kwargs)
        self.name = None
        self.is_data_action = None
        self.display = display
        self.origin = None
        self.action_type = None


class OperationDisplay(_serialization.Model):
    """Localized display information for this particular operation.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar provider: The localized friendly form of the resource provider name, e.g. "Microsoft
     Monitoring Insights" or "Microsoft Compute".
    :vartype provider: str
    :ivar resource: The localized friendly name of the resource type related to this operation.
     E.g. "Virtual Machines" or "Job Schedule Collections".
    :vartype resource: str
    :ivar operation: The concise, localized friendly name for the operation; suitable for
     dropdowns. E.g. "Create or Update Virtual Machine", "Restart Virtual Machine".
    :vartype operation: str
    :ivar description: The short, localized friendly description of the operation; suitable for
     tool tips and detailed views.
    :vartype description: str
    """

    _validation = {
        "provider": {"readonly": True},
        "resource": {"readonly": True},
        "operation": {"readonly": True},
        "description": {"readonly": True},
    }

    _attribute_map = {
        "provider": {"key": "provider", "type": "str"},
        "resource": {"key": "resource", "type": "str"},
        "operation": {"key": "operation", "type": "str"},
        "description": {"key": "description", "type": "str"},
    }

    def __init__(self, **kwargs: Any) -> None:
        """ """
        super().__init__(**kwargs)
        self.provider = None
        self.resource = None
        self.operation = None
        self.description = None


class OperationListResult(_serialization.Model):
    """A list of REST API operations supported by an Azure Resource Provider. It contains an URL link
    to get the next set of results.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar value: List of operations supported by the resource provider.
    :vartype value: list[~azure.mgmt.qumulo.models.Operation]
    :ivar next_link: URL to get the next set of operation list results (if there are any).
    :vartype next_link: str
    """

    _validation = {
        "value": {"readonly": True},
        "next_link": {"readonly": True},
    }

    _attribute_map = {
        "value": {"key": "value", "type": "[Operation]"},
        "next_link": {"key": "nextLink", "type": "str"},
    }

    def __init__(self, **kwargs: Any) -> None:
        """ """
        super().__init__(**kwargs)
        self.value = None
        self.next_link = None


class SystemData(_serialization.Model):
    """Metadata pertaining to creation and last modification of the resource.

    :ivar created_by: The identity that created the resource.
    :vartype created_by: str
    :ivar created_by_type: The type of identity that created the resource. Known values are:
     "User", "Application", "ManagedIdentity", and "Key".
    :vartype created_by_type: str or ~azure.mgmt.qumulo.models.CreatedByType
    :ivar created_at: The timestamp of resource creation (UTC).
    :vartype created_at: ~datetime.datetime
    :ivar last_modified_by: The identity that last modified the resource.
    :vartype last_modified_by: str
    :ivar last_modified_by_type: The type of identity that last modified the resource. Known values
     are: "User", "Application", "ManagedIdentity", and "Key".
    :vartype last_modified_by_type: str or ~azure.mgmt.qumulo.models.CreatedByType
    :ivar last_modified_at: The timestamp of resource last modification (UTC).
    :vartype last_modified_at: ~datetime.datetime
    """

    _attribute_map = {
        "created_by": {"key": "createdBy", "type": "str"},
        "created_by_type": {"key": "createdByType", "type": "str"},
        "created_at": {"key": "createdAt", "type": "iso-8601"},
        "last_modified_by": {"key": "lastModifiedBy", "type": "str"},
        "last_modified_by_type": {"key": "lastModifiedByType", "type": "str"},
        "last_modified_at": {"key": "lastModifiedAt", "type": "iso-8601"},
    }

    def __init__(
        self,
        *,
        created_by: Optional[str] = None,
        created_by_type: Optional[Union[str, "_models.CreatedByType"]] = None,
        created_at: Optional[datetime.datetime] = None,
        last_modified_by: Optional[str] = None,
        last_modified_by_type: Optional[Union[str, "_models.CreatedByType"]] = None,
        last_modified_at: Optional[datetime.datetime] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword created_by: The identity that created the resource.
        :paramtype created_by: str
        :keyword created_by_type: The type of identity that created the resource. Known values are:
         "User", "Application", "ManagedIdentity", and "Key".
        :paramtype created_by_type: str or ~azure.mgmt.qumulo.models.CreatedByType
        :keyword created_at: The timestamp of resource creation (UTC).
        :paramtype created_at: ~datetime.datetime
        :keyword last_modified_by: The identity that last modified the resource.
        :paramtype last_modified_by: str
        :keyword last_modified_by_type: The type of identity that last modified the resource. Known
         values are: "User", "Application", "ManagedIdentity", and "Key".
        :paramtype last_modified_by_type: str or ~azure.mgmt.qumulo.models.CreatedByType
        :keyword last_modified_at: The timestamp of resource last modification (UTC).
        :paramtype last_modified_at: ~datetime.datetime
        """
        super().__init__(**kwargs)
        self.created_by = created_by
        self.created_by_type = created_by_type
        self.created_at = created_at
        self.last_modified_by = last_modified_by
        self.last_modified_by_type = last_modified_by_type
        self.last_modified_at = last_modified_at


class UserAssignedIdentity(_serialization.Model):
    """User assigned identity properties.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar principal_id: The principal ID of the assigned identity.
    :vartype principal_id: str
    :ivar client_id: The client ID of the assigned identity.
    :vartype client_id: str
    """

    _validation = {
        "principal_id": {"readonly": True},
        "client_id": {"readonly": True},
    }

    _attribute_map = {
        "principal_id": {"key": "principalId", "type": "str"},
        "client_id": {"key": "clientId", "type": "str"},
    }

    def __init__(self, **kwargs: Any) -> None:
        """ """
        super().__init__(**kwargs)
        self.principal_id = None
        self.client_id = None


class UserDetails(_serialization.Model):
    """User Details of Qumulo FileSystem resource.

    All required parameters must be populated in order to send to server.

    :ivar email: User Email. Required.
    :vartype email: str
    """

    _validation = {
        "email": {"required": True},
    }

    _attribute_map = {
        "email": {"key": "email", "type": "str"},
    }

    def __init__(self, *, email: str, **kwargs: Any) -> None:
        """
        :keyword email: User Email. Required.
        :paramtype email: str
        """
        super().__init__(**kwargs)
        self.email = email
