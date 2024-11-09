# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class ActiveRevisionsMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """ActiveRevisionsMode controls how active revisions are handled for the Container app:


    .. raw:: html

       <list><item>Multiple: multiple revisions can be active. If no value if provided, this is the
    default</item><item>Single: Only one revision can be active at a time. Revision weights can not
    be used in this mode</item></list>.
    """

    MULTIPLE = "multiple"
    SINGLE = "single"


class AppServicePlanRestrictions(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """App Service plans this offer is restricted to."""

    NONE = "None"
    FREE = "Free"
    SHARED = "Shared"
    BASIC = "Basic"
    STANDARD = "Standard"
    PREMIUM = "Premium"


class AutoHealActionType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Predefined action to be taken."""

    RECYCLE = "Recycle"
    LOG_EVENT = "LogEvent"
    CUSTOM_ACTION = "CustomAction"


class AzureResourceType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of the Azure resource the hostname is assigned to."""

    WEBSITE = "Website"
    TRAFFIC_MANAGER = "TrafficManager"


class AzureStorageState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """State of the storage account."""

    OK = "Ok"
    INVALID_CREDENTIALS = "InvalidCredentials"
    INVALID_SHARE = "InvalidShare"
    NOT_VALIDATED = "NotValidated"


class AzureStorageType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of storage."""

    AZURE_FILES = "AzureFiles"
    AZURE_BLOB = "AzureBlob"


class BackupItemStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Backup status."""

    IN_PROGRESS = "InProgress"
    FAILED = "Failed"
    SUCCEEDED = "Succeeded"
    TIMED_OUT = "TimedOut"
    CREATED = "Created"
    SKIPPED = "Skipped"
    PARTIALLY_SUCCEEDED = "PartiallySucceeded"
    DELETE_IN_PROGRESS = "DeleteInProgress"
    DELETE_FAILED = "DeleteFailed"
    DELETED = "Deleted"


class BackupRestoreOperationType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Operation type."""

    DEFAULT = "Default"
    CLONE = "Clone"
    RELOCATION = "Relocation"
    SNAPSHOT = "Snapshot"
    CLOUD_FS = "CloudFS"


class BasicAuthName(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """BasicAuthName."""

    DEFAULT = "default"


class BuildStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The status of the static site build."""

    WAITING_FOR_DEPLOYMENT = "WaitingForDeployment"
    UPLOADING = "Uploading"
    DEPLOYING = "Deploying"
    READY = "Ready"
    FAILED = "Failed"
    DELETING = "Deleting"
    DETACHED = "Detached"


class BuiltInAuthenticationProvider(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The default authentication provider to use when multiple providers are configured.
    This setting is only needed if multiple providers are configured and the unauthenticated client
    action is set to "RedirectToLoginPage".
    """

    AZURE_ACTIVE_DIRECTORY = "AzureActiveDirectory"
    FACEBOOK = "Facebook"
    GOOGLE = "Google"
    MICROSOFT_ACCOUNT = "MicrosoftAccount"
    TWITTER = "Twitter"
    GITHUB = "Github"


class CertificateOrderActionType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Action type."""

    CERTIFICATE_ISSUED = "CertificateIssued"
    CERTIFICATE_ORDER_CANCELED = "CertificateOrderCanceled"
    CERTIFICATE_ORDER_CREATED = "CertificateOrderCreated"
    CERTIFICATE_REVOKED = "CertificateRevoked"
    DOMAIN_VALIDATION_COMPLETE = "DomainValidationComplete"
    FRAUD_DETECTED = "FraudDetected"
    ORG_NAME_CHANGE = "OrgNameChange"
    ORG_VALIDATION_COMPLETE = "OrgValidationComplete"
    SAN_DROP = "SanDrop"
    FRAUD_CLEARED = "FraudCleared"
    CERTIFICATE_EXPIRED = "CertificateExpired"
    CERTIFICATE_EXPIRATION_WARNING = "CertificateExpirationWarning"
    FRAUD_DOCUMENTATION_REQUIRED = "FraudDocumentationRequired"
    UNKNOWN = "Unknown"


class CertificateOrderStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Current order status."""

    PENDINGISSUANCE = "Pendingissuance"
    ISSUED = "Issued"
    REVOKED = "Revoked"
    CANCELED = "Canceled"
    DENIED = "Denied"
    PENDINGREVOCATION = "Pendingrevocation"
    PENDING_REKEY = "PendingRekey"
    UNUSED = "Unused"
    EXPIRED = "Expired"
    NOT_SUBMITTED = "NotSubmitted"


class CertificateProductType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Certificate product type."""

    STANDARD_DOMAIN_VALIDATED_SSL = "StandardDomainValidatedSsl"
    STANDARD_DOMAIN_VALIDATED_WILD_CARD_SSL = "StandardDomainValidatedWildCardSsl"


class Channels(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """List of channels that this recommendation can apply."""

    NOTIFICATION = "Notification"
    API = "Api"
    EMAIL = "Email"
    WEBHOOK = "Webhook"
    ALL = "All"


class CheckNameResourceTypes(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Resource type used for verification."""

    SITE = "Site"
    SLOT = "Slot"
    HOSTING_ENVIRONMENT = "HostingEnvironment"
    PUBLISHING_USER = "PublishingUser"
    MICROSOFT_WEB_SITES = "Microsoft.Web/sites"
    MICROSOFT_WEB_SITES_SLOTS = "Microsoft.Web/sites/slots"
    MICROSOFT_WEB_HOSTING_ENVIRONMENTS = "Microsoft.Web/hostingEnvironments"
    MICROSOFT_WEB_PUBLISHING_USERS = "Microsoft.Web/publishingUsers"


class ClientCertMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """This composes with ClientCertEnabled setting.


    * ClientCertEnabled: false means ClientCert is ignored.
    * ClientCertEnabled: true and ClientCertMode: Required means ClientCert is required.
    * ClientCertEnabled: true and ClientCertMode: Optional means ClientCert is optional or
    accepted.
    """

    REQUIRED = "Required"
    OPTIONAL = "Optional"
    OPTIONAL_INTERACTIVE_USER = "OptionalInteractiveUser"


class CloneAbilityResult(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Name of app."""

    CLONEABLE = "Cloneable"
    PARTIALLY_CLONEABLE = "PartiallyCloneable"
    NOT_CLONEABLE = "NotCloneable"


class ComputeModeOptions(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Shared/dedicated workers."""

    SHARED = "Shared"
    DEDICATED = "Dedicated"
    DYNAMIC = "Dynamic"


class ConnectionStringType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of database."""

    MY_SQL = "MySql"
    SQL_SERVER = "SQLServer"
    SQL_AZURE = "SQLAzure"
    CUSTOM = "Custom"
    NOTIFICATION_HUB = "NotificationHub"
    SERVICE_BUS = "ServiceBus"
    EVENT_HUB = "EventHub"
    API_HUB = "ApiHub"
    DOC_DB = "DocDb"
    REDIS_CACHE = "RedisCache"
    POSTGRE_SQL = "PostgreSQL"


class ContainerAppProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Provisioning state of the Container App."""

    IN_PROGRESS = "InProgress"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"


class ContinuousWebJobStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Job status."""

    INITIALIZING = "Initializing"
    STARTING = "Starting"
    RUNNING = "Running"
    PENDING_RESTART = "PendingRestart"
    STOPPED = "Stopped"


class CookieExpirationConvention(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The convention used when determining the session cookie's expiration."""

    FIXED_TIME = "FixedTime"
    IDENTITY_PROVIDER_DERIVED = "IdentityProviderDerived"


class CustomDnsSuffixProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """CustomDnsSuffixProvisioningState."""

    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    DEGRADED = "Degraded"
    IN_PROGRESS = "InProgress"


class CustomDomainStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The status of the custom domain."""

    RETRIEVING_VALIDATION_TOKEN = "RetrievingValidationToken"
    VALIDATING = "Validating"
    ADDING = "Adding"
    READY = "Ready"
    FAILED = "Failed"
    DELETING = "Deleting"
    UNHEALTHY = "Unhealthy"


class CustomHostNameDnsRecordType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of the DNS record."""

    C_NAME = "CName"
    A = "A"


class DaprLogLevel(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Sets the log level for the Dapr sidecar. Allowed values are debug, info, warn, error. Default
    is info.
    """

    INFO = "info"
    DEBUG = "debug"
    WARN = "warn"
    ERROR = "error"


class DatabaseType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Database type (e.g. SqlAzure / MySql)."""

    SQL_AZURE = "SqlAzure"
    MY_SQL = "MySql"
    LOCAL_MY_SQL = "LocalMySql"
    POSTGRE_SQL = "PostgreSql"


class DayOfWeek(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The day of the week."""

    SUNDAY = "Sunday"
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"


class DaysOfWeek(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """DaysOfWeek."""

    SUNDAY = "Sunday"
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"


class DefaultAction(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Default action for main access restriction if no rules are matched."""

    ALLOW = "Allow"
    DENY = "Deny"


class DeploymentBuildStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Deployment build status."""

    TIMED_OUT = "TimedOut"
    RUNTIME_FAILED = "RuntimeFailed"
    BUILD_ABORTED = "BuildAborted"
    BUILD_FAILED = "BuildFailed"
    BUILD_REQUEST_RECEIVED = "BuildRequestReceived"
    BUILD_PENDING = "BuildPending"
    BUILD_IN_PROGRESS = "BuildInProgress"
    BUILD_SUCCESSFUL = "BuildSuccessful"
    POST_BUILD_RESTART_REQUIRED = "PostBuildRestartRequired"
    START_POLLING = "StartPolling"
    START_POLLING_WITH_RESTART = "StartPollingWithRestart"
    RUNTIME_STARTING = "RuntimeStarting"
    RUNTIME_SUCCESSFUL = "RuntimeSuccessful"


class DetectorType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Whether this detector is an Analysis Detector or not."""

    DETECTOR = "Detector"
    ANALYSIS = "Analysis"
    CATEGORY_OVERVIEW = "CategoryOverview"


class DnsType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Current DNS type."""

    AZURE_DNS = "AzureDns"
    DEFAULT_DOMAIN_REGISTRAR_DNS = "DefaultDomainRegistrarDns"


class DnsVerificationTestResult(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """DNS verification test result."""

    PASSED = "Passed"
    FAILED = "Failed"
    SKIPPED = "Skipped"


class DomainStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Domain registration status."""

    ACTIVE = "Active"
    AWAITING = "Awaiting"
    CANCELLED = "Cancelled"
    CONFISCATED = "Confiscated"
    DISABLED = "Disabled"
    EXCLUDED = "Excluded"
    EXPIRED = "Expired"
    FAILED = "Failed"
    HELD = "Held"
    LOCKED = "Locked"
    PARKED = "Parked"
    PENDING = "Pending"
    RESERVED = "Reserved"
    REVERTED = "Reverted"
    SUSPENDED = "Suspended"
    TRANSFERRED = "Transferred"
    UNKNOWN = "Unknown"
    UNLOCKED = "Unlocked"
    UNPARKED = "Unparked"
    UPDATED = "Updated"
    JSON_CONVERTER_FAILED = "JsonConverterFailed"


class DomainType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Valid values are Regular domain: Azure will charge the full price of domain registration,
    SoftDeleted: Purchasing this domain will simply restore it and this operation will not cost
    anything.
    """

    REGULAR = "Regular"
    SOFT_DELETED = "SoftDeleted"


class EnterpriseGradeCdnStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """State indicating the status of the enterprise grade CDN serving traffic to the static web app."""

    ENABLED = "Enabled"
    ENABLING = "Enabling"
    DISABLED = "Disabled"
    DISABLING = "Disabling"


class ForwardProxyConvention(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The convention used to determine the url of the request made."""

    NO_PROXY = "NoProxy"
    STANDARD = "Standard"
    CUSTOM = "Custom"


class FrequencyUnit(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The unit of time for how often the backup should be executed (e.g. for weekly backup, this
    should be set to Day and FrequencyInterval should be set to 7).
    """

    DAY = "Day"
    HOUR = "Hour"


class FrontEndServiceType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """FrontEndServiceType."""

    NODE_PORT = "NodePort"
    LOAD_BALANCER = "LoadBalancer"


class FtpsState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """State of FTP / FTPS service."""

    ALL_ALLOWED = "AllAllowed"
    FTPS_ONLY = "FtpsOnly"
    DISABLED = "Disabled"


class HostingEnvironmentStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Current status of the App Service Environment."""

    PREPARING = "Preparing"
    READY = "Ready"
    SCALING = "Scaling"
    DELETING = "Deleting"


class HostNameType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of the hostname."""

    VERIFIED = "Verified"
    MANAGED = "Managed"


class HostType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Indicates whether the hostname is a standard or repository hostname."""

    STANDARD = "Standard"
    REPOSITORY = "Repository"


class InAvailabilityReasonType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """:code:`<code>Invalid</code>` indicates the name provided does not match Azure App Service
    naming requirements. :code:`<code>AlreadyExists</code>` indicates that the name is already in
    use and is therefore unavailable.
    """

    INVALID = "Invalid"
    ALREADY_EXISTS = "AlreadyExists"


class IngressTransportMethod(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Ingress transport protocol."""

    AUTO = "auto"
    HTTP = "http"
    HTTP2 = "http2"


class InsightStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Level of the most severe insight generated by the detector."""

    CRITICAL = "Critical"
    WARNING = "Warning"
    INFO = "Info"
    SUCCESS = "Success"
    NONE = "None"


class IpFilterTag(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Defines what this IP filter will be used for. This is to support IP filtering on proxies."""

    DEFAULT = "Default"
    XFF_PROXY = "XffProxy"
    SERVICE_TAG = "ServiceTag"


class IssueType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Represents the type of the Detector."""

    SERVICE_INCIDENT = "ServiceIncident"
    APP_DEPLOYMENT = "AppDeployment"
    APP_CRASH = "AppCrash"
    RUNTIME_ISSUE_DETECTED = "RuntimeIssueDetected"
    ASE_DEPLOYMENT = "AseDeployment"
    USER_ISSUE = "UserIssue"
    PLATFORM_ISSUE = "PlatformIssue"
    OTHER = "Other"


class KeyType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The key type."""

    NOT_SPECIFIED = "NotSpecified"
    PRIMARY = "Primary"
    SECONDARY = "Secondary"


class KeyVaultSecretStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Status of the Key Vault secret."""

    INITIALIZED = "Initialized"
    WAITING_ON_CERTIFICATE_ORDER = "WaitingOnCertificateOrder"
    SUCCEEDED = "Succeeded"
    CERTIFICATE_ORDER_FAILED = "CertificateOrderFailed"
    OPERATION_NOT_PERMITTED_ON_KEY_VAULT = "OperationNotPermittedOnKeyVault"
    AZURE_SERVICE_UNAUTHORIZED_TO_ACCESS_KEY_VAULT = "AzureServiceUnauthorizedToAccessKeyVault"
    KEY_VAULT_DOES_NOT_EXIST = "KeyVaultDoesNotExist"
    KEY_VAULT_SECRET_DOES_NOT_EXIST = "KeyVaultSecretDoesNotExist"
    UNKNOWN_ERROR = "UnknownError"
    EXTERNAL_PRIVATE_KEY = "ExternalPrivateKey"
    UNKNOWN = "Unknown"


class Kind(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The workflow kind."""

    STATEFUL = "Stateful"
    STATELESS = "Stateless"


class KubeEnvironmentProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Provisioning state of the Kubernetes Environment."""

    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"
    WAITING = "Waiting"
    INITIALIZATION_IN_PROGRESS = "InitializationInProgress"
    INFRASTRUCTURE_SETUP_IN_PROGRESS = "InfrastructureSetupInProgress"
    INFRASTRUCTURE_SETUP_COMPLETE = "InfrastructureSetupComplete"
    SCHEDULED_FOR_DELETE = "ScheduledForDelete"
    UPGRADE_REQUESTED = "UpgradeRequested"
    UPGRADE_FAILED = "UpgradeFailed"


class LoadBalancingMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Specifies which endpoints to serve internally in the Virtual Network for the App Service
    Environment.
    """

    NONE = "None"
    WEB = "Web"
    PUBLISHING = "Publishing"
    WEB_PUBLISHING = "Web, Publishing"


class LogLevel(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Log level."""

    OFF = "Off"
    VERBOSE = "Verbose"
    INFORMATION = "Information"
    WARNING = "Warning"
    ERROR = "Error"


class ManagedPipelineMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Managed pipeline mode."""

    INTEGRATED = "Integrated"
    CLASSIC = "Classic"


class ManagedServiceIdentityType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of managed service identity."""

    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned, UserAssigned"
    NONE = "None"


class MSDeployLogEntryType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Log entry type."""

    MESSAGE = "Message"
    WARNING = "Warning"
    ERROR = "Error"


class MSDeployProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Provisioning state."""

    ACCEPTED = "accepted"
    RUNNING = "running"
    SUCCEEDED = "succeeded"
    FAILED = "failed"
    CANCELED = "canceled"


class MySqlMigrationType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of migration operation to be done."""

    LOCAL_TO_REMOTE = "LocalToRemote"
    REMOTE_TO_LOCAL = "RemoteToLocal"


class NotificationLevel(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Level indicating how critical this recommendation can impact."""

    CRITICAL = "Critical"
    WARNING = "Warning"
    INFORMATION = "Information"
    NON_URGENT_SUGGESTION = "NonUrgentSuggestion"


class OpenAuthenticationProviderType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Open authentication policy provider type."""

    AAD = "AAD"


class OperationStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The current status of the operation."""

    IN_PROGRESS = "InProgress"
    FAILED = "Failed"
    SUCCEEDED = "Succeeded"
    TIMED_OUT = "TimedOut"
    CREATED = "Created"


class ParameterType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The parameter type."""

    NOT_SPECIFIED = "NotSpecified"
    STRING = "String"
    SECURE_STRING = "SecureString"
    INT = "Int"
    FLOAT = "Float"
    BOOL = "Bool"
    ARRAY = "Array"
    OBJECT = "Object"
    SECURE_OBJECT = "SecureObject"
    INT_ENUM = "Int"


class ProviderOsTypeSelected(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """ProviderOsTypeSelected."""

    WINDOWS = "Windows"
    LINUX = "Linux"
    WINDOWS_FUNCTIONS = "WindowsFunctions"
    LINUX_FUNCTIONS = "LinuxFunctions"
    ALL = "All"


class ProviderStackOsType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """ProviderStackOsType."""

    WINDOWS = "Windows"
    LINUX = "Linux"
    ALL = "All"


class ProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Status of certificate order."""

    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"
    IN_PROGRESS = "InProgress"
    DELETING = "Deleting"


class PublicCertificateLocation(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Public Certificate Location."""

    CURRENT_USER_MY = "CurrentUserMy"
    LOCAL_MACHINE_MY = "LocalMachineMy"
    UNKNOWN = "Unknown"


class PublishingProfileFormat(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Name of the format. Valid values are:
    FileZilla3
    WebDeploy -- default
    Ftp.
    """

    FILE_ZILLA3 = "FileZilla3"
    WEB_DEPLOY = "WebDeploy"
    FTP = "Ftp"


class RecurrenceFrequency(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The recurrence frequency."""

    NOT_SPECIFIED = "NotSpecified"
    SECOND = "Second"
    MINUTE = "Minute"
    HOUR = "Hour"
    DAY = "Day"
    WEEK = "Week"
    MONTH = "Month"
    YEAR = "Year"


class RedundancyMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Site redundancy mode."""

    NONE = "None"
    MANUAL = "Manual"
    FAILOVER = "Failover"
    ACTIVE_ACTIVE = "ActiveActive"
    GEO_REDUNDANT = "GeoRedundant"


class RenderingType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Rendering Type."""

    NO_GRAPH = "NoGraph"
    TABLE = "Table"
    TIME_SERIES = "TimeSeries"
    TIME_SERIES_PER_INSTANCE = "TimeSeriesPerInstance"
    PIE_CHART = "PieChart"
    DATA_SUMMARY = "DataSummary"
    EMAIL = "Email"
    INSIGHTS = "Insights"
    DYNAMIC_INSIGHT = "DynamicInsight"
    MARKDOWN = "Markdown"
    DETECTOR = "Detector"
    DROP_DOWN = "DropDown"
    CARD = "Card"
    SOLUTION = "Solution"
    GUAGE = "Guage"
    FORM = "Form"
    CHANGE_SETS = "ChangeSets"
    CHANGE_ANALYSIS_ONBOARDING = "ChangeAnalysisOnboarding"
    CHANGES_VIEW = "ChangesView"
    APP_INSIGHT = "AppInsight"
    DEPENDENCY_GRAPH = "DependencyGraph"
    DOWN_TIME = "DownTime"
    SUMMARY_CARD = "SummaryCard"
    SEARCH_COMPONENT = "SearchComponent"
    APP_INSIGHT_ENABLEMENT = "AppInsightEnablement"


class ResolveStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """ResolveStatus."""

    INITIALIZED = "Initialized"
    RESOLVED = "Resolved"
    INVALID_SYNTAX = "InvalidSyntax"
    MSI_NOT_ENABLED = "MSINotEnabled"
    VAULT_NOT_FOUND = "VaultNotFound"
    SECRET_NOT_FOUND = "SecretNotFound"
    SECRET_VERSION_NOT_FOUND = "SecretVersionNotFound"
    ACCESS_TO_KEY_VAULT_DENIED = "AccessToKeyVaultDenied"
    OTHER_REASONS = "OtherReasons"
    FETCH_TIMED_OUT = "FetchTimedOut"
    UNAUTHORIZED_CLIENT = "UnauthorizedClient"


class ResourceNotRenewableReason(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """ResourceNotRenewableReason."""

    REGISTRATION_STATUS_NOT_SUPPORTED_FOR_RENEWAL = "RegistrationStatusNotSupportedForRenewal"
    EXPIRATION_NOT_IN_RENEWAL_TIME_RANGE = "ExpirationNotInRenewalTimeRange"
    SUBSCRIPTION_NOT_ACTIVE = "SubscriptionNotActive"


class ResourceScopeType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Name of a resource type this recommendation applies, e.g. Subscription, ServerFarm, Site."""

    SERVER_FARM = "ServerFarm"
    SUBSCRIPTION = "Subscription"
    WEB_SITE = "WebSite"


class RevisionHealthState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Current health State of the revision."""

    HEALTHY = "Healthy"
    UNHEALTHY = "Unhealthy"
    NONE = "None"


class RevisionProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Current provisioning State of the revision."""

    PROVISIONING = "Provisioning"
    PROVISIONED = "Provisioned"
    FAILED = "Failed"
    DEPROVISIONING = "Deprovisioning"
    DEPROVISIONED = "Deprovisioned"


class RouteType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of route this is:
    DEFAULT - By default, every app has routes to the local address ranges specified by RFC1918
    INHERITED - Routes inherited from the real Virtual Network routes
    STATIC - Static route set on the app only

    These values will be used for syncing an app's routes with those from a Virtual Network.
    """

    DEFAULT = "DEFAULT"
    INHERITED = "INHERITED"
    STATIC = "STATIC"


class ScmType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """SCM type."""

    NONE = "None"
    DROPBOX = "Dropbox"
    TFS = "Tfs"
    LOCAL_GIT = "LocalGit"
    GIT_HUB = "GitHub"
    CODE_PLEX_GIT = "CodePlexGit"
    CODE_PLEX_HG = "CodePlexHg"
    BITBUCKET_GIT = "BitbucketGit"
    BITBUCKET_HG = "BitbucketHg"
    EXTERNAL_GIT = "ExternalGit"
    EXTERNAL_HG = "ExternalHg"
    ONE_DRIVE = "OneDrive"
    VSO = "VSO"
    VSTSRM = "VSTSRM"


class SiteAvailabilityState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Management information availability state for the app."""

    NORMAL = "Normal"
    LIMITED = "Limited"
    DISASTER_RECOVERY_MODE = "DisasterRecoveryMode"


class SiteExtensionType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Site extension type."""

    GALLERY = "Gallery"
    WEB_ROOT = "WebRoot"


class SiteLoadBalancing(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Site load balancing."""

    WEIGHTED_ROUND_ROBIN = "WeightedRoundRobin"
    LEAST_REQUESTS = "LeastRequests"
    LEAST_RESPONSE_TIME = "LeastResponseTime"
    WEIGHTED_TOTAL_TRAFFIC = "WeightedTotalTraffic"
    REQUEST_HASH = "RequestHash"
    PER_SITE_ROUND_ROBIN = "PerSiteRoundRobin"


class SiteRuntimeState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """SiteRuntimeState."""

    READY = "READY"
    STOPPED = "STOPPED"
    UNKNOWN = "UNKNOWN"


class SkuName(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """SkuName."""

    FREE = "Free"
    SHARED = "Shared"
    BASIC = "Basic"
    STANDARD = "Standard"
    PREMIUM = "Premium"
    DYNAMIC = "Dynamic"
    ISOLATED = "Isolated"
    ISOLATED_V2 = "IsolatedV2"
    PREMIUM_V2 = "PremiumV2"
    PREMIUM_V3 = "PremiumV3"
    PREMIUM_CONTAINER = "PremiumContainer"
    ELASTIC_PREMIUM = "ElasticPremium"
    ELASTIC_ISOLATED = "ElasticIsolated"


class SolutionType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of Solution."""

    QUICK_SOLUTION = "QuickSolution"
    DEEP_INVESTIGATION = "DeepInvestigation"
    BEST_PRACTICES = "BestPractices"


class SslState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """SSL type."""

    DISABLED = "Disabled"
    SNI_ENABLED = "SniEnabled"
    IP_BASED_ENABLED = "IpBasedEnabled"


class StackPreferredOs(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Function App stack preferred OS."""

    WINDOWS = "Windows"
    LINUX = "Linux"


class StagingEnvironmentPolicy(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """State indicating whether staging environments are allowed or not allowed for a static web app."""

    ENABLED = "Enabled"
    DISABLED = "Disabled"


class StatusOptions(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """App Service plan status."""

    READY = "Ready"
    PENDING = "Pending"
    CREATING = "Creating"


class StorageType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """StorageType."""

    LOCAL_NODE = "LocalNode"
    NETWORK_FILE_SYSTEM = "NetworkFileSystem"


class SupportedTlsVersions(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """MinTlsVersion: configures the minimum version of TLS required for SSL requests."""

    ONE0 = "1.0"
    ONE1 = "1.1"
    ONE2 = "1.2"


class TlsCipherSuites(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The minimum strength TLS cipher suite allowed for an application."""

    TLS_AES256_GCM_SHA384 = "TLS_AES_256_GCM_SHA384"
    TLS_AES128_GCM_SHA256 = "TLS_AES_128_GCM_SHA256"
    TLS_ECDHE_ECDSA_WITH_AES256_GCM_SHA384 = "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384"
    TLS_ECDHE_ECDSA_WITH_AES128_CBC_SHA256 = "TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256"
    TLS_ECDHE_ECDSA_WITH_AES128_GCM_SHA256 = "TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256"
    TLS_ECDHE_RSA_WITH_AES256_GCM_SHA384 = "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384"
    TLS_ECDHE_RSA_WITH_AES128_GCM_SHA256 = "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256"
    TLS_ECDHE_RSA_WITH_AES256_CBC_SHA384 = "TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384"
    TLS_ECDHE_RSA_WITH_AES128_CBC_SHA256 = "TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256"
    TLS_ECDHE_RSA_WITH_AES256_CBC_SHA = "TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA"
    TLS_ECDHE_RSA_WITH_AES128_CBC_SHA = "TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA"
    TLS_RSA_WITH_AES256_GCM_SHA384 = "TLS_RSA_WITH_AES_256_GCM_SHA384"
    TLS_RSA_WITH_AES128_GCM_SHA256 = "TLS_RSA_WITH_AES_128_GCM_SHA256"
    TLS_RSA_WITH_AES256_CBC_SHA256 = "TLS_RSA_WITH_AES_256_CBC_SHA256"
    TLS_RSA_WITH_AES128_CBC_SHA256 = "TLS_RSA_WITH_AES_128_CBC_SHA256"
    TLS_RSA_WITH_AES256_CBC_SHA = "TLS_RSA_WITH_AES_256_CBC_SHA"
    TLS_RSA_WITH_AES128_CBC_SHA = "TLS_RSA_WITH_AES_128_CBC_SHA"


class TriggeredWebJobStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Job status."""

    SUCCESS = "Success"
    FAILED = "Failed"
    ERROR = "Error"


class TriggerTypes(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The trigger type of the function."""

    HTTP_TRIGGER = "HttpTrigger"
    UNKNOWN = "Unknown"


class UnauthenticatedClientAction(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The action to take when an unauthenticated client attempts to access the app."""

    REDIRECT_TO_LOGIN_PAGE = "RedirectToLoginPage"
    ALLOW_ANONYMOUS = "AllowAnonymous"


class UnauthenticatedClientActionV2(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The action to take when an unauthenticated client attempts to access the app."""

    REDIRECT_TO_LOGIN_PAGE = "RedirectToLoginPage"
    ALLOW_ANONYMOUS = "AllowAnonymous"
    RETURN401 = "Return401"
    RETURN403 = "Return403"


class UpgradeAvailability(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Whether an upgrade is available for this App Service Environment."""

    NONE = "None"
    """No upgrade is currently available for this App Service Environment"""
    READY = "Ready"
    """An upgrade is ready to be manually initiated on this App Service Environment"""


class UpgradePreference(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Upgrade Preference."""

    NONE = "None"
    """No preference on when this App Service Environment will be upgraded"""
    EARLY = "Early"
    """This App Service Environment will be upgraded before others in the same region that have
    Upgrade Preference 'Late'"""
    LATE = "Late"
    """This App Service Environment will be upgraded after others in the same region that have Upgrade
    Preference 'Early'"""
    MANUAL = "Manual"
    """ASEv3 only. Once an upgrade is available, this App Service Environment will wait 10 days for
    the upgrade to be manually initiated. After 10 days the upgrade will begin automatically"""


class UsageState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """State indicating whether the app has exceeded its quota usage. Read-only."""

    NORMAL = "Normal"
    EXCEEDED = "Exceeded"


class ValidateResourceTypes(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Resource type used for verification."""

    SERVER_FARM = "ServerFarm"
    SITE = "Site"
    MICROSOFT_WEB_HOSTING_ENVIRONMENTS = "Microsoft.Web/hostingEnvironments"


class WebJobType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Job type."""

    CONTINUOUS = "Continuous"
    TRIGGERED = "Triggered"


class WorkerSizeOptions(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Size of the machines."""

    SMALL = "Small"
    MEDIUM = "Medium"
    LARGE = "Large"
    D1 = "D1"
    D2 = "D2"
    D3 = "D3"
    SMALL_V3 = "SmallV3"
    MEDIUM_V3 = "MediumV3"
    LARGE_V3 = "LargeV3"
    NESTED_SMALL = "NestedSmall"
    NESTED_SMALL_LINUX = "NestedSmallLinux"
    DEFAULT = "Default"


class WorkflowHealthState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Gets or sets the workflow health state."""

    NOT_SPECIFIED = "NotSpecified"
    HEALTHY = "Healthy"
    UNHEALTHY = "Unhealthy"
    UNKNOWN = "Unknown"


class WorkflowProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The workflow provisioning state."""

    NOT_SPECIFIED = "NotSpecified"
    ACCEPTED = "Accepted"
    RUNNING = "Running"
    READY = "Ready"
    CREATING = "Creating"
    CREATED = "Created"
    DELETING = "Deleting"
    DELETED = "Deleted"
    CANCELED = "Canceled"
    FAILED = "Failed"
    SUCCEEDED = "Succeeded"
    MOVING = "Moving"
    UPDATING = "Updating"
    REGISTERING = "Registering"
    REGISTERED = "Registered"
    UNREGISTERING = "Unregistering"
    UNREGISTERED = "Unregistered"
    COMPLETED = "Completed"
    RENEWING = "Renewing"
    PENDING = "Pending"
    WAITING = "Waiting"
    IN_PROGRESS = "InProgress"


class WorkflowSkuName(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The sku name."""

    NOT_SPECIFIED = "NotSpecified"
    FREE = "Free"
    SHARED = "Shared"
    BASIC = "Basic"
    STANDARD = "Standard"
    PREMIUM = "Premium"


class WorkflowState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The workflow state."""

    NOT_SPECIFIED = "NotSpecified"
    COMPLETED = "Completed"
    ENABLED = "Enabled"
    DISABLED = "Disabled"
    DELETED = "Deleted"
    SUSPENDED = "Suspended"


class WorkflowStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The workflow status."""

    NOT_SPECIFIED = "NotSpecified"
    PAUSED = "Paused"
    RUNNING = "Running"
    WAITING = "Waiting"
    SUCCEEDED = "Succeeded"
    SKIPPED = "Skipped"
    SUSPENDED = "Suspended"
    CANCELLED = "Cancelled"
    FAILED = "Failed"
    FAULTED = "Faulted"
    TIMED_OUT = "TimedOut"
    ABORTED = "Aborted"
    IGNORED = "Ignored"


class WorkflowTriggerProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The workflow trigger provisioning state."""

    NOT_SPECIFIED = "NotSpecified"
    ACCEPTED = "Accepted"
    RUNNING = "Running"
    READY = "Ready"
    CREATING = "Creating"
    CREATED = "Created"
    DELETING = "Deleting"
    DELETED = "Deleted"
    CANCELED = "Canceled"
    FAILED = "Failed"
    SUCCEEDED = "Succeeded"
    MOVING = "Moving"
    UPDATING = "Updating"
    REGISTERING = "Registering"
    REGISTERED = "Registered"
    UNREGISTERING = "Unregistering"
    UNREGISTERED = "Unregistered"
    COMPLETED = "Completed"
