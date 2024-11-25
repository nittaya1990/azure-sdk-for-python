# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class ActionType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Extensible enum. Indicates the action type. "Internal" refers to actions that are for internal
    only APIs.
    """

    INTERNAL = "Internal"
    """Actions are for internal-only APIs."""


class Origin(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The intended executor of the operation; as in Resource Based Access Control (RBAC) and audit
    logs UX. Default value is "user,system".
    """

    USER = "user"
    """Indicates the operation is initiated by a user."""
    SYSTEM = "system"
    """Indicates the operation is initiated by a system."""
    USER_SYSTEM = "user,system"
    """Indicates the operation is initiated by a user or system."""


class ResourceProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The provisioning state of a resource type."""

    SUCCEEDED = "Succeeded"
    """Resource has been created."""
    FAILED = "Failed"
    """Resource creation failed."""
    CANCELED = "Canceled"
    """Resource creation was canceled."""


class TargetProvider(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The target Azure Terraform Provider."""

    AZURERM = "azurerm"
    """https://registry.terraform.io/providers/hashicorp/azurerm/latest"""
    AZAPI = "azapi"
    """https://registry.terraform.io/providers/Azure/azapi/latest"""


class Type(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The parameter type."""

    EXPORT_RESOURCE = "ExportResource"
    EXPORT_RESOURCE_GROUP = "ExportResourceGroup"
    EXPORT_QUERY = "ExportQuery"
