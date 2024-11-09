# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class CachingTypes(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Specifies the caching requirements. :code:`<br>`:code:`<br>` Possible values are:
    :code:`<br>`:code:`<br>` **None** :code:`<br>`:code:`<br>` **ReadOnly**
    :code:`<br>`:code:`<br>` **ReadWrite** :code:`<br>`:code:`<br>` Default: **None for Standard
    storage. ReadOnly for Premium storage**.
    """

    NONE = "None"
    READ_ONLY = "ReadOnly"
    READ_WRITE = "ReadWrite"


class DiskCreateOptionTypes(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Specifies how the virtual machine should be created.:code:`<br>`:code:`<br>` Possible values
    are::code:`<br>`:code:`<br>` **Attach** \\u2013 This value is used when you are using a
    specialized disk to create the virtual machine.:code:`<br>`:code:`<br>` **FromImage** \\u2013
    This value is used when you are using an image to create the virtual machine. If you are using
    a platform image, you also use the imageReference element described above. If you are using a
    marketplace image, you  also use the plan element previously described.
    """

    FROM_IMAGE = "FromImage"
    EMPTY = "Empty"
    ATTACH = "Attach"


class OperatingSystemTypes(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The operating system of the osDiskImage."""

    WINDOWS = "Windows"
    LINUX = "Linux"


class ProtocolTypes(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Specifies the protocol of listener. :code:`<br>`:code:`<br>` Possible values are:
    :code:`<br>`\\ **http** :code:`<br>`:code:`<br>` **https**.
    """

    HTTP = "Http"
    HTTPS = "Https"


class SettingNames(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Specifies the name of the setting to which the content applies. Possible values are:
    FirstLogonCommands and AutoLogon.
    """

    AUTO_LOGON = "AutoLogon"
    FIRST_LOGON_COMMANDS = "FirstLogonCommands"


class StatusLevelTypes(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The level code."""

    INFO = "Info"
    WARNING = "Warning"
    ERROR = "Error"


class UpgradeMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Specifies the mode of an upgrade to virtual machines in the scale set.:code:`<br />`:code:`<br
    />` Possible values are::code:`<br />`:code:`<br />` **Manual** - You  control the application
    of updates to virtual machines in the scale set. You do this by using the manualUpgrade
    action.:code:`<br />`:code:`<br />` **Automatic** - All virtual machines in the scale set are
    automatically updated at the same time.
    """

    AUTOMATIC = "Automatic"
    MANUAL = "Manual"


class VirtualMachineScaleSetSkuScaleType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The scale type applicable to the sku."""

    AUTOMATIC = "Automatic"
    NONE = "None"


class VirtualMachineSizeTypes(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Specifies the size of the virtual machine. For more information about virtual machine sizes,
    see `Sizes for virtual machines
    <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-sizes?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json>`_.
    :code:`<br>`:code:`<br>` The available VM sizes depend on region and availability set. For a
    list of available sizes use these APIs:  :code:`<br>`:code:`<br>` `List all available virtual
    machine sizes in an availability set
    <https://docs.microsoft.com/rest/api/compute/availabilitysets/listavailablesizes>`_
    :code:`<br>`:code:`<br>` `List all available virtual machine sizes in a region
    <https://docs.microsoft.com/rest/api/compute/virtualmachinesizes/list>`_
    :code:`<br>`:code:`<br>` `List all available virtual machine sizes for resizing
    <https://docs.microsoft.com/rest/api/compute/virtualmachines/listavailablesizes>`_.
    """

    BASIC_A0 = "Basic_A0"
    BASIC_A1 = "Basic_A1"
    BASIC_A2 = "Basic_A2"
    BASIC_A3 = "Basic_A3"
    BASIC_A4 = "Basic_A4"
    STANDARD_A0 = "Standard_A0"
    STANDARD_A1 = "Standard_A1"
    STANDARD_A2 = "Standard_A2"
    STANDARD_A3 = "Standard_A3"
    STANDARD_A4 = "Standard_A4"
    STANDARD_A5 = "Standard_A5"
    STANDARD_A6 = "Standard_A6"
    STANDARD_A7 = "Standard_A7"
    STANDARD_A8 = "Standard_A8"
    STANDARD_A9 = "Standard_A9"
    STANDARD_A10 = "Standard_A10"
    STANDARD_A11 = "Standard_A11"
    STANDARD_D1 = "Standard_D1"
    STANDARD_D2 = "Standard_D2"
    STANDARD_D3 = "Standard_D3"
    STANDARD_D4 = "Standard_D4"
    STANDARD_D11 = "Standard_D11"
    STANDARD_D12 = "Standard_D12"
    STANDARD_D13 = "Standard_D13"
    STANDARD_D14 = "Standard_D14"
    STANDARD_D1_V2 = "Standard_D1_v2"
    STANDARD_D2_V2 = "Standard_D2_v2"
    STANDARD_D3_V2 = "Standard_D3_v2"
    STANDARD_D4_V2 = "Standard_D4_v2"
    STANDARD_D5_V2 = "Standard_D5_v2"
    STANDARD_D11_V2 = "Standard_D11_v2"
    STANDARD_D12_V2 = "Standard_D12_v2"
    STANDARD_D13_V2 = "Standard_D13_v2"
    STANDARD_D14_V2 = "Standard_D14_v2"
    STANDARD_DS1 = "Standard_DS1"
    STANDARD_DS2 = "Standard_DS2"
    STANDARD_DS3 = "Standard_DS3"
    STANDARD_DS4 = "Standard_DS4"
    STANDARD_DS11 = "Standard_DS11"
    STANDARD_DS12 = "Standard_DS12"
    STANDARD_DS13 = "Standard_DS13"
    STANDARD_DS14 = "Standard_DS14"
    STANDARD_G1 = "Standard_G1"
    STANDARD_G2 = "Standard_G2"
    STANDARD_G3 = "Standard_G3"
    STANDARD_G4 = "Standard_G4"
    STANDARD_G5 = "Standard_G5"
    STANDARD_GS1 = "Standard_GS1"
    STANDARD_GS2 = "Standard_GS2"
    STANDARD_GS3 = "Standard_GS3"
    STANDARD_GS4 = "Standard_GS4"
    STANDARD_GS5 = "Standard_GS5"
