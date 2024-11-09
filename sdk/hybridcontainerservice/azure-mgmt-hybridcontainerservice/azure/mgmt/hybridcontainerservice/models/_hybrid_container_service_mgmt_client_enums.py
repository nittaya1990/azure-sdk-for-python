# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class ActionType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Enum. Indicates the action type. "Internal" refers to actions that are for internal only APIs."""

    INTERNAL = "Internal"


class AddonPhase(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Observed phase of the addon or component on the provisioned cluster. Possible values include:
    'pending', 'provisioning', 'provisioning {HelmChartInstalled}', 'provisioning
    {MSICertificateDownloaded}', 'provisioned', 'deleting', 'failed', 'upgrading'.
    """

    PENDING = "pending"
    PROVISIONING = "provisioning"
    PROVISIONING_HELM_CHART_INSTALLED_ = "provisioning {HelmChartInstalled}"
    PROVISIONING_MSI_CERTIFICATE_DOWNLOADED_ = "provisioning {MSICertificateDownloaded}"
    PROVISIONED = "provisioned"
    DELETING = "deleting"
    FAILED = "failed"
    UPGRADING = "upgrading"


class AzureHybridBenefit(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Indicates whether Azure Hybrid Benefit is opted in. Default value is false."""

    TRUE = "True"
    FALSE = "False"
    NOT_APPLICABLE = "NotApplicable"


class CreatedByType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of identity that created the resource."""

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"


class Expander(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """If not specified, the default is 'random'. See `expanders
    <https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md#what-are-expanders>`_
    for more information.
    """

    LEAST_WASTE = "least-waste"
    """Selects the node group that will have the least idle CPU (if tied, unused memory) after
    #: scale-up. This is useful when you have different classes of nodes, for example, high CPU or
    #: high memory nodes, and only want to expand those when there are pending pods that need a lot of
    #: those resources."""
    MOST_PODS = "most-pods"
    """Selects the node group that would be able to schedule the most pods when scaling up. This is
    #: useful when you are using nodeSelector to make sure certain pods land on certain nodes. Note
    #: that this won't cause the autoscaler to select bigger nodes vs. smaller, as it can add multiple
    #: smaller nodes at once."""
    PRIORITY = "priority"
    """Selects the node group that has the highest priority assigned by the user. It's configuration
    #: is described in more details `here
    #: <https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/expander/priority/readme.md>`_."""
    RANDOM = "random"
    """Used when you don't have a particular need for the node groups to scale differently."""


class ExtendedLocationTypes(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The extended location type. Allowed value: 'CustomLocation'."""

    CUSTOM_LOCATION = "CustomLocation"


class NetworkPolicy(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Network policy used for building Kubernetes network. Possible values include: 'calico'."""

    CALICO = "calico"


class Origin(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The intended executor of the operation; as in Resource Based Access Control (RBAC) and audit
    logs UX. Default value is "user,system".
    """

    USER = "user"
    SYSTEM = "system"
    USER_SYSTEM = "user,system"


class OSSKU(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Specifies the OS SKU used by the agent pool. The default is CBLMariner if OSType is Linux. The
    default is Windows2019 when OSType is Windows.
    """

    CBL_MARINER = "CBLMariner"
    """Use Mariner as the OS for node images."""
    WINDOWS2019 = "Windows2019"
    """Use Windows2019 as the OS for node images."""
    WINDOWS2022 = "Windows2022"
    """Use Windows2022 as the OS for node images."""


class OsType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The particular KubernetesVersion Image OS Type (Linux, Windows)."""

    WINDOWS = "Windows"
    LINUX = "Linux"


class ProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """ProvisioningState."""

    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"
    PENDING = "Pending"
    CREATING = "Creating"
    DELETING = "Deleting"
    UPDATING = "Updating"
    ACCEPTED = "Accepted"


class ResourceProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Provisioning state of the resource."""

    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"
    PENDING = "Pending"
    CREATING = "Creating"
    DELETING = "Deleting"
    UPDATING = "Updating"
    UPGRADING = "Upgrading"
    ACCEPTED = "Accepted"
