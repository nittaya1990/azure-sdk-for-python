# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import CheckNameAvailabilityResult
from ._models_py3 import CustomDomain
from ._models_py3 import Encryption
from ._models_py3 import EncryptionService
from ._models_py3 import EncryptionServices
from ._models_py3 import Endpoints
from ._models_py3 import Resource
from ._models_py3 import Sku
from ._models_py3 import StorageAccount
from ._models_py3 import StorageAccountCheckNameAvailabilityParameters
from ._models_py3 import StorageAccountCreateParameters
from ._models_py3 import StorageAccountKey
from ._models_py3 import StorageAccountListKeysResult
from ._models_py3 import StorageAccountListResult
from ._models_py3 import StorageAccountRegenerateKeyParameters
from ._models_py3 import StorageAccountUpdateParameters
from ._models_py3 import Usage
from ._models_py3 import UsageListResult
from ._models_py3 import UsageName

from ._storage_management_client_enums import AccessTier
from ._storage_management_client_enums import AccountStatus
from ._storage_management_client_enums import EncryptionKeySource
from ._storage_management_client_enums import KeyPermission
from ._storage_management_client_enums import Kind
from ._storage_management_client_enums import ProvisioningState
from ._storage_management_client_enums import Reason
from ._storage_management_client_enums import SkuName
from ._storage_management_client_enums import SkuTier
from ._storage_management_client_enums import StorageAccountCheckNameAvailabilityParametersType
from ._storage_management_client_enums import UsageUnit
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "CheckNameAvailabilityResult",
    "CustomDomain",
    "Encryption",
    "EncryptionService",
    "EncryptionServices",
    "Endpoints",
    "Resource",
    "Sku",
    "StorageAccount",
    "StorageAccountCheckNameAvailabilityParameters",
    "StorageAccountCreateParameters",
    "StorageAccountKey",
    "StorageAccountListKeysResult",
    "StorageAccountListResult",
    "StorageAccountRegenerateKeyParameters",
    "StorageAccountUpdateParameters",
    "Usage",
    "UsageListResult",
    "UsageName",
    "AccessTier",
    "AccountStatus",
    "EncryptionKeySource",
    "KeyPermission",
    "Kind",
    "ProvisioningState",
    "Reason",
    "SkuName",
    "SkuTier",
    "StorageAccountCheckNameAvailabilityParametersType",
    "UsageUnit",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
