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


class AutonomousDatabaseBackupLifecycleState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Autonomous database backup lifecycle state enum."""

    CREATING = "Creating"
    """AutonomousDatabase backup is creating"""
    ACTIVE = "Active"
    """AutonomousDatabase backup is active"""
    DELETING = "Deleting"
    """AutonomousDatabase backup is deleting"""
    FAILED = "Failed"
    """AutonomousDatabase backup is failed"""
    UPDATING = "Updating"
    """AutonomousDatabase backup is updating"""


class AutonomousDatabaseBackupType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Autonomous database backup type enum."""

    INCREMENTAL = "Incremental"
    """Incremental backup"""
    FULL = "Full"
    """Full backup"""
    LONG_TERM = "LongTerm"
    """LongTerm backup"""


class AutonomousDatabaseLifecycleState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Autonomous database lifecycle state enum."""

    PROVISIONING = "Provisioning"
    """Indicates that resource in Provisioning state"""
    AVAILABLE = "Available"
    """Indicates that resource in Available state"""
    STOPPING = "Stopping"
    """Indicates that resource in Stopping state"""
    STOPPED = "Stopped"
    """Indicates that resource in Stopped state"""
    STARTING = "Starting"
    """Indicates that resource in Starting state"""
    TERMINATING = "Terminating"
    """Indicates that resource in Terminating state"""
    TERMINATED = "Terminated"
    """Indicates that resource in Terminated state"""
    UNAVAILABLE = "Unavailable"
    """Indicates that resource in Unavailable state"""
    RESTORE_IN_PROGRESS = "RestoreInProgress"
    """Indicates that resource in RestoreInProgress state"""
    RESTORE_FAILED = "RestoreFailed"
    """Indicates that resource in RestoreFailed state"""
    BACKUP_IN_PROGRESS = "BackupInProgress"
    """Indicates that resource in BackupInProgress state"""
    SCALE_IN_PROGRESS = "ScaleInProgress"
    """Indicates that resource in ScaleInProgress state"""
    AVAILABLE_NEEDS_ATTENTION = "AvailableNeedsAttention"
    """Indicates that resource is available but needs attention"""
    UPDATING = "Updating"
    """Indicates that resource in Updating state"""
    MAINTENANCE_IN_PROGRESS = "MaintenanceInProgress"
    """Indicates that resource maintenance in progress state"""
    RESTARTING = "Restarting"
    """Indicates that resource in Restarting state"""
    RECREATING = "Recreating"
    """Indicates that resource in Recreating state"""
    ROLE_CHANGE_IN_PROGRESS = "RoleChangeInProgress"
    """Indicates that resource role change in progress state"""
    UPGRADING = "Upgrading"
    """Indicates that resource in Upgrading state"""
    INACCESSIBLE = "Inaccessible"
    """IIndicates that resource in Inaccessible state"""
    STANDBY = "Standby"
    """Indicates that resource in Standby state"""


class AutonomousMaintenanceScheduleType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Autonomous database maintenance schedule type enum."""

    EARLY = "Early"
    """Early maintenance schedule"""
    REGULAR = "Regular"
    """Regular maintenance schedule"""


class AzureResourceProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Azure Resource Provisioning State enum."""

    SUCCEEDED = "Succeeded"
    """Resource has been created."""
    FAILED = "Failed"
    """Resource creation failed."""
    CANCELED = "Canceled"
    """Resource creation was canceled."""
    PROVISIONING = "Provisioning"
    """Indicates that resource in Provisioning state"""


class CloneType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Clone type enum."""

    FULL = "Full"
    """Full clone"""
    METADATA = "Metadata"
    """Metadata only"""


class CloudAccountProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """CloudAccountProvisioningState enum."""

    PENDING = "Pending"
    """Pending - Initial state when Oracle cloud account is not configured"""
    PROVISIONING = "Provisioning"
    """Provisioning - State when Oracle cloud account is being provisioned"""
    AVAILABLE = "Available"
    """Available - State when Oracle cloud account cloud linking is complete and it is available"""


class CloudExadataInfrastructureLifecycleState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """CloudExadataInfrastructureLifecycleState enum."""

    PROVISIONING = "Provisioning"
    """Indicates that resource in Provisioning state"""
    AVAILABLE = "Available"
    """Indicates that resource in Available state"""
    UPDATING = "Updating"
    """Indicates that resource in Updating state"""
    TERMINATING = "Terminating"
    """Indicates that resource in Terminating state"""
    TERMINATED = "Terminated"
    """Indicates that resource in Terminated state"""
    MAINTENANCE_IN_PROGRESS = "MaintenanceInProgress"
    """Indicates that resource maintenance in progress state"""
    FAILED = "Failed"
    """Indicates that resource in Failed state"""


class CloudVmClusterLifecycleState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Cloud VM Cluster lifecycle state enum."""

    PROVISIONING = "Provisioning"
    """Indicates that resource in Provisioning state"""
    AVAILABLE = "Available"
    """Indicates that resource in Available state"""
    UPDATING = "Updating"
    """Indicates that resource in Updating state"""
    TERMINATING = "Terminating"
    """Indicates that resource in Terminating state"""
    TERMINATED = "Terminated"
    """Indicates that resource in Terminated state"""
    MAINTENANCE_IN_PROGRESS = "MaintenanceInProgress"
    """Indicates that resource Maintenance in progress state"""
    FAILED = "Failed"
    """Indicates that resource in Failed state"""


class ComputeModel(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Compute model enum."""

    ECPU = "ECPU"
    """ECPU model type"""
    OCPU = "OCPU"
    """OCPU model type"""


class ConsumerGroup(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Consumer group enum."""

    HIGH = "High"
    """High group"""
    MEDIUM = "Medium"
    """Medium group"""
    LOW = "Low"
    """Low group"""
    TP = "Tp"
    """TP group"""
    TPURGENT = "Tpurgent"
    """TPurgent group"""


class CreatedByType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of identity that created the resource."""

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"


class DatabaseEditionType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Database edition type enum."""

    STANDARD_EDITION = "StandardEdition"
    """Standard edition"""
    ENTERPRISE_EDITION = "EnterpriseEdition"
    """Enterprise edition"""


class DataBaseType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Database type enum."""

    REGULAR = "Regular"
    """Regular DB"""
    CLONE = "Clone"
    """Clone DB"""


class DataSafeStatusType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """DataSafe status type enum."""

    REGISTERING = "Registering"
    """Registering status"""
    REGISTERED = "Registered"
    """Registered status"""
    DEREGISTERING = "Deregistering"
    """Deregistering status"""
    NOT_REGISTERED = "NotRegistered"
    """NotRegistered status"""
    FAILED = "Failed"
    """Failed status"""


class DayOfWeekName(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """DayOfWeekName enum."""

    MONDAY = "Monday"
    """Monday value"""
    TUESDAY = "Tuesday"
    """Tuesday value"""
    WEDNESDAY = "Wednesday"
    """Wednesday value"""
    THURSDAY = "Thursday"
    """Thursday value"""
    FRIDAY = "Friday"
    """Friday value"""
    SATURDAY = "Saturday"
    """Saturday value"""
    SUNDAY = "Sunday"
    """Sunday value"""


class DbNodeActionEnum(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """DbNode action enum."""

    START = "Start"
    """Start DbNode"""
    STOP = "Stop"
    """Stop DbNode"""
    SOFT_RESET = "SoftReset"
    """Soft reset DbNode"""
    RESET = "Reset"
    """Reset DbNode"""


class DbNodeMaintenanceType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of database node maintenance."""

    VMDB_REBOOT_MIGRATION = "VmdbRebootMigration"
    """VMDB reboot migration maintenance type"""


class DbNodeProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """DnNode provisioning state enum."""

    PROVISIONING = "Provisioning"
    """Indicates that resource in Provisioning state"""
    AVAILABLE = "Available"
    """Indicates that resource in Available state"""
    UPDATING = "Updating"
    """Indicates that resource in Updating state"""
    STOPPING = "Stopping"
    """Indicates that resource in Stopping state"""
    STOPPED = "Stopped"
    """Indicates that resource in Stopped state"""
    STARTING = "Starting"
    """Indicates that resource in Starting state"""
    TERMINATING = "Terminating"
    """Indicates that resource in Terminating state"""
    TERMINATED = "Terminated"
    """Indicates that resource in Terminated state"""
    FAILED = "Failed"
    """Indicates that resource in Failed state"""


class DbServerPatchingStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """DB Server patching status enum."""

    SCHEDULED = "Scheduled"
    """Patching scheduled"""
    MAINTENANCE_IN_PROGRESS = "MaintenanceInProgress"
    """Patching in progress"""
    FAILED = "Failed"
    """Patching failed"""
    COMPLETE = "Complete"
    """Patching completed"""


class DbServerProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """DbServerProvisioningState enum."""

    CREATING = "Creating"
    """Indicates that resource in Creating state"""
    AVAILABLE = "Available"
    """Indicates that resource in Available state"""
    UNAVAILABLE = "Unavailable"
    """Indicates that resource in Unavailable state"""
    DELETING = "Deleting"
    """Indicates that resource in Deleting state"""
    DELETED = "Deleted"
    """Indicates that resource in Deleted state"""
    MAINTENANCE_IN_PROGRESS = "MaintenanceInProgress"
    """Indicates that resource maintenance in progress state"""


class DisasterRecoveryType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Disaster recovery type enum."""

    ADG = "Adg"
    """ADG type"""
    BACKUP_BASED = "BackupBased"
    """Backup based type"""


class DiskRedundancy(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Disk redundancy enum."""

    HIGH = "High"
    """High redundancy"""
    NORMAL = "Normal"
    """Normal redundancy"""


class DnsPrivateViewsLifecycleState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """DNS Private Views lifecycle state enum."""

    ACTIVE = "Active"
    """DNS Private View is active"""
    DELETED = "Deleted"
    """DNS Private View is deleted"""
    DELETING = "Deleting"
    """DNS Private View is deleting"""
    UPDATING = "Updating"
    """DNS Private View is updating"""


class DnsPrivateZonesLifecycleState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """DNS Private Zones lifecycle state enum."""

    ACTIVE = "Active"
    """DNS Private Zones is active"""
    CREATING = "Creating"
    """DNS Private Zones is creating"""
    DELETED = "Deleted"
    """DNS Private Zones is deleted"""
    DELETING = "Deleting"
    """DNS Private Zones is deleting"""
    UPDATING = "Updating"
    """DNS Private Zones is updating"""


class GenerateType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Generate type enum."""

    SINGLE = "Single"
    """Generate single"""
    ALL = "All"
    """Generate all"""


class HostFormatType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Host format type enum."""

    FQDN = "Fqdn"
    """FQDN format"""
    IP = "Ip"
    """IP format"""


class Intent(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Intent enum."""

    RETAIN = "Retain"
    """Retain intent"""
    RESET = "Reset"
    """Reset intent"""


class IormLifecycleState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """ORM lifecycle state enum."""

    BOOT_STRAPPING = "BootStrapping"
    """Indicates that resource in Provisioning state"""
    ENABLED = "Enabled"
    """Indicates that resource in Enabled state"""
    DISABLED = "Disabled"
    """Indicates that resource in Disabled state"""
    UPDATING = "Updating"
    """Indicates that resource in Updating state"""
    FAILED = "Failed"
    """Indicates that resource in Failed state"""


class LicenseModel(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """LicenseModel enum."""

    LICENSE_INCLUDED = "LicenseIncluded"
    """License included"""
    BRING_YOUR_OWN_LICENSE = "BringYourOwnLicense"
    """Bring Your Own License"""


class MonthName(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """MonthName enum."""

    JANUARY = "January"
    """January value"""
    FEBRUARY = "February"
    """February value"""
    MARCH = "March"
    """March value"""
    APRIL = "April"
    """April value"""
    MAY = "May"
    """May value"""
    JUNE = "June"
    """June value"""
    JULY = "July"
    """July value"""
    AUGUST = "August"
    """August value"""
    SEPTEMBER = "September"
    """September value"""
    OCTOBER = "October"
    """October value"""
    NOVEMBER = "November"
    """November value"""
    DECEMBER = "December"
    """December value"""


class Objective(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Objective enum."""

    LOW_LATENCY = "LowLatency"
    """Low latency objective"""
    HIGH_THROUGHPUT = "HighThroughput"
    """High throughput objective"""
    BALANCED = "Balanced"
    """Balanced objective"""
    AUTO = "Auto"
    """Auto objective"""
    BASIC = "Basic"
    """Basic objective"""


class OpenModeType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Open mode type enum."""

    READ_ONLY = "ReadOnly"
    """ReadOnly mode"""
    READ_WRITE = "ReadWrite"
    """ReadWrite mode"""


class OperationsInsightsStatusType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Operations Insights status type enum."""

    ENABLING = "Enabling"
    """Enabling status"""
    ENABLED = "Enabled"
    """Enabled status"""
    DISABLING = "Disabling"
    """Disabling status"""
    NOT_ENABLED = "NotEnabled"
    """NotEnabled status"""
    FAILED_ENABLING = "FailedEnabling"
    """FailedEnabling status"""
    FAILED_DISABLING = "FailedDisabling"
    """FailedDisabling status"""


class OracleSubscriptionProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """OracleSubscriptionProvisioningState enum."""

    SUCCEEDED = "Succeeded"
    """Resource has been created."""
    FAILED = "Failed"
    """Resource creation failed."""
    CANCELED = "Canceled"
    """Resource creation was canceled."""


class Origin(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The intended executor of the operation; as in Resource Based Access Control (RBAC) and audit
    logs UX. Default value is "user,system".
    """

    USER = "user"
    SYSTEM = "system"
    USER_SYSTEM = "user,system"


class PatchingMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Patching mode enum."""

    ROLLING = "Rolling"
    """Rolling patching"""
    NON_ROLLING = "NonRolling"
    """Non Rolling patching"""


class PermissionLevelType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Permission level type enum."""

    RESTRICTED = "Restricted"
    """Restricted permission level"""
    UNRESTRICTED = "Unrestricted"
    """Unrestricted permission level"""


class Preference(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Preference enum."""

    NO_PREFERENCE = "NoPreference"
    """No preference"""
    CUSTOM_PREFERENCE = "CustomPreference"
    """Custom preference"""


class ProtocolType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Protocol type enum."""

    TCP = "TCP"
    """TCP protocol"""
    TCPS = "TCPS"
    """TCPS protocol"""


class RefreshableModelType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Refreshable model type enum."""

    AUTOMATIC = "Automatic"
    """Automatic refreshable model type"""
    MANUAL = "Manual"
    """Manual refreshable model type"""


class RefreshableStatusType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Refreshable status type enum."""

    REFRESHING = "Refreshing"
    """Refreshing status"""
    NOT_REFRESHING = "NotRefreshing"
    """NotRefreshing status"""


class RepeatCadenceType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Repeat cadence type enum."""

    ONE_TIME = "OneTime"
    """Repeat one time"""
    WEEKLY = "Weekly"
    """Repeat weekly"""
    MONTHLY = "Monthly"
    """Repeat monthly"""
    YEARLY = "Yearly"
    """Repeat yearly"""


class ResourceProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The provisioning state of a resource type."""

    SUCCEEDED = "Succeeded"
    """Resource has been created."""
    FAILED = "Failed"
    """Resource creation failed."""
    CANCELED = "Canceled"
    """Resource creation was canceled."""


class RoleType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Role type enum."""

    PRIMARY = "Primary"
    """Primary role"""
    STANDBY = "Standby"
    """Standby role"""
    DISABLED_STANDBY = "DisabledStandby"
    """DisabledStandby role"""
    BACKUP_COPY = "BackupCopy"
    """BackupCopy role"""
    SNAPSHOT_STANDBY = "SnapshotStandby"
    """SnapshotStandby role"""


class SessionModeType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Session mode type enum."""

    DIRECT = "Direct"
    """Direct session mode"""
    REDIRECT = "Redirect"
    """Redirect session mode"""


class SourceType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Source type enum."""

    NONE = "None"
    """None source"""
    DATABASE = "Database"
    """Database source"""
    BACKUP_FROM_ID = "BackupFromId"
    """Backup from ID source"""
    BACKUP_FROM_TIMESTAMP = "BackupFromTimestamp"
    """Backup from timestamp source"""
    CLONE_TO_REFRESHABLE = "CloneToRefreshable"
    """Clone to refreshable source"""
    CROSS_REGION_DATAGUARD = "CrossRegionDataguard"
    """Cross region dataguard source"""
    CROSS_REGION_DISASTER_RECOVERY = "CrossRegionDisasterRecovery"
    """cross region disaster recovery source"""


class SyntaxFormatType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Syntax format type enum."""

    LONG = "Long"
    """Long format"""
    EZCONNECT = "Ezconnect"
    """Ezconnect format"""
    EZCONNECTPLUS = "Ezconnectplus"
    """Ezconnectplus format"""


class TlsAuthenticationType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """TLS authentication type enum."""

    SERVER = "Server"
    """Server authentication"""
    MUTUAL = "Mutual"
    """Mutual TLS"""


class UpdateAction(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Update action enum."""

    ROLLING_APPLY = "RollingApply"
    """Rolling apply action"""
    NON_ROLLING_APPLY = "NonRollingApply"
    """Non rolling apply action"""
    PRE_CHECK = "PreCheck"
    """Pre-check action"""
    ROLL_BACK = "RollBack"
    """Rollback action"""


class ValidationStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """validation status."""

    SUCCEEDED = "Succeeded"
    """Validation succeeded"""
    FAILED = "Failed"
    """Validation failed"""


class VirtualNetworkAddressLifecycleState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """VirtualNetworkAddressLifecycleState enum."""

    PROVISIONING = "Provisioning"
    """Indicates that resource in Provisioning state"""
    AVAILABLE = "Available"
    """Indicates that resource in Available state"""
    TERMINATING = "Terminating"
    """Indicates that resource in Terminating state"""
    TERMINATED = "Terminated"
    """Indicates that resource in Terminated state"""
    FAILED = "Failed"
    """Indicates that resource in Failed state"""


class WorkloadType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """WorkloadType enum."""

    OLTP = "OLTP"
    """OLTP - indicates an Autonomous Transaction Processing database"""
    DW = "DW"
    """DW - indicates an Autonomous Data Warehouse database"""
    AJD = "AJD"
    """AJD - indicates an Autonomous JSON Database"""
    APEX = "APEX"
    """APEX - indicates an Autonomous Database with the Oracle APEX Application Development workload
    type."""


class ZoneType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Zone type enum."""

    PRIMARY = "Primary"
    """Primary zone"""
    SECONDARY = "Secondary"
    """Secondary zone"""
