# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models import CancelOperationsRequest
from ._models import CancelOperationsResponse
from ._models import DeallocateResourceOperationResponse
from ._models import ErrorAdditionalInfo
from ._models import ErrorDetail
from ._models import ErrorResponse
from ._models import ExecuteDeallocateRequest
from ._models import ExecuteHibernateRequest
from ._models import ExecuteStartRequest
from ._models import ExecutionParameters
from ._models import GetOperationErrorsRequest
from ._models import GetOperationErrorsResponse
from ._models import GetOperationStatusRequest
from ._models import GetOperationStatusResponse
from ._models import HibernateResourceOperationResponse
from ._models import Operation
from ._models import OperationDisplay
from ._models import OperationErrorDetails
from ._models import OperationErrorsResult
from ._models import ResourceOperation
from ._models import ResourceOperationDetails
from ._models import ResourceOperationError
from ._models import Resources
from ._models import RetryPolicy
from ._models import Schedule
from ._models import StartResourceOperationResponse
from ._models import SubmitDeallocateRequest
from ._models import SubmitHibernateRequest
from ._models import SubmitStartRequest

from ._enums import ActionType
from ._enums import DeadlineType
from ._enums import OperationState
from ._enums import OptimizationPreference
from ._enums import Origin
from ._enums import ResourceOperationType
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "CancelOperationsRequest",
    "CancelOperationsResponse",
    "DeallocateResourceOperationResponse",
    "ErrorAdditionalInfo",
    "ErrorDetail",
    "ErrorResponse",
    "ExecuteDeallocateRequest",
    "ExecuteHibernateRequest",
    "ExecuteStartRequest",
    "ExecutionParameters",
    "GetOperationErrorsRequest",
    "GetOperationErrorsResponse",
    "GetOperationStatusRequest",
    "GetOperationStatusResponse",
    "HibernateResourceOperationResponse",
    "Operation",
    "OperationDisplay",
    "OperationErrorDetails",
    "OperationErrorsResult",
    "ResourceOperation",
    "ResourceOperationDetails",
    "ResourceOperationError",
    "Resources",
    "RetryPolicy",
    "Schedule",
    "StartResourceOperationResponse",
    "SubmitDeallocateRequest",
    "SubmitHibernateRequest",
    "SubmitStartRequest",
    "ActionType",
    "DeadlineType",
    "OperationState",
    "OptimizationPreference",
    "Origin",
    "ResourceOperationType",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
