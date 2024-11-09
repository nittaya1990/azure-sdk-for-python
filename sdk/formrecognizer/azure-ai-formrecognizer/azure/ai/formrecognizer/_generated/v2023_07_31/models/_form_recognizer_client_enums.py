# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class AnalyzeResultOperationStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Operation status.
    """

    #: The operation has not started yet.
    NOT_STARTED = "notStarted"
    #: The operation is in progress.
    RUNNING = "running"
    #: The operation has failed.
    FAILED = "failed"
    #: The operation has succeeded.
    SUCCEEDED = "succeeded"

class ContentType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Content type for upload
    """

    #: Content Type 'application/octet-stream'.
    APPLICATION_OCTET_STREAM = "application/octet-stream"
    #: Content Type 'application/pdf'.
    APPLICATION_PDF = "application/pdf"
    #: Content Type 'application/vnd.openxmlformats-officedocument.presentationml.presentation'.
    APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_PRESENTATIONML_PRESENTATION = "application/vnd.openxmlformats-officedocument.presentationml.presentation"
    #: Content Type 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'.
    APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_SPREADSHEETML_SHEET = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    #: Content Type 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'.
    APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_WORDPROCESSINGML_DOCUMENT = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    #: Content Type 'image/bmp'.
    IMAGE_BMP = "image/bmp"
    #: Content Type 'image/heif'.
    IMAGE_HEIF = "image/heif"
    #: Content Type 'image/jpeg'.
    IMAGE_JPEG = "image/jpeg"
    #: Content Type 'image/png'.
    IMAGE_PNG = "image/png"
    #: Content Type 'image/tiff'.
    IMAGE_TIFF = "image/tiff"
    #: Content Type 'text/html'.
    TEXT_HTML = "text/html"

class DocumentAnalysisFeature(str, Enum, metaclass=CaseInsensitiveEnumMeta):

    #: Perform OCR at a higher resolution to handle documents with fine print.
    OCR_HIGH_RESOLUTION = "ocrHighResolution"
    #: Enable the detection of the text content language.
    LANGUAGES = "languages"
    #: Enable the detection of barcodes in the document.
    BARCODES = "barcodes"
    #: Enable the detection of mathematical expressions in the document.
    FORMULAS = "formulas"
    #: Enable the detection of general key value pairs (form fields) in the document.
    KEY_VALUE_PAIRS = "keyValuePairs"
    #: Enable the recognition of various font styles.
    STYLE_FONT = "styleFont"

class DocumentBarcodeKind(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Barcode kind.
    """

    #: QR code, as defined in ISO/IEC 18004:2015.
    QR_CODE = "QRCode"
    #: PDF417, as defined in ISO 15438.
    PDF417 = "PDF417"
    #: GS1 12-digit Universal Product Code.
    UPCA = "UPCA"
    #: GS1 6-digit Universal Product Code.
    UPCE = "UPCE"
    #: Code 39 barcode, as defined in ISO/IEC 16388:2007.
    CODE39 = "Code39"
    #: Code 128 barcode, as defined in ISO/IEC 15417:2007.
    CODE128 = "Code128"
    #: GS1 8-digit International Article Number (European Article Number).
    EAN8 = "EAN8"
    #: GS1 13-digit International Article Number (European Article Number).
    EAN13 = "EAN13"
    #: GS1 DataBar barcode.
    DATA_BAR = "DataBar"
    #: Code 93 barcode, as defined in ANSI/AIM BC5-1995.
    CODE93 = "Code93"
    #: Codabar barcode, as defined in ANSI/AIM BC3-1995.
    CODABAR = "Codabar"
    #: GS1 DataBar Expanded barcode.
    DATA_BAR_EXPANDED = "DataBarExpanded"
    #: Interleaved 2 of 5 barcode, as defined in ANSI/AIM BC2-1995.
    ITF = "ITF"
    #: Micro QR code, as defined in ISO/IEC 23941:2022.
    MICRO_QR_CODE = "MicroQRCode"
    #: Aztec code, as defined in ISO/IEC 24778:2008.
    AZTEC = "Aztec"
    #: Data matrix code, as defined in ISO/IEC 16022:2006.
    DATA_MATRIX = "DataMatrix"
    #: MaxiCode, as defined in ISO/IEC 16023:2000.
    MAXI_CODE = "MaxiCode"

class DocumentBuildMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Custom document model build mode.
    """

    #: Target documents with similar visual templates.
    TEMPLATE = "template"
    #: Support documents with diverse visual templates.
    NEURAL = "neural"

class DocumentFieldType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Semantic data type of the field value.
    """

    #: Plain text.
    STRING = "string"
    #: Date, normalized to ISO 8601 (YYYY-MM-DD) format.
    DATE = "date"
    #: Time, normalized to ISO 8601 (hh:mm:ss) format.
    TIME = "time"
    #: Phone number, normalized to E.164 (+{CountryCode}{SubscriberNumber}) format.
    PHONE_NUMBER = "phoneNumber"
    #: Floating point number, normalized to double precision floating point.
    NUMBER = "number"
    #: Integer number, normalized to 64-bit signed integer.
    INTEGER = "integer"
    #: Is field selected?.
    SELECTION_MARK = "selectionMark"
    #: Country/region, normalized to ISO 3166-1 alpha-3 format (ex. USA).
    COUNTRY_REGION = "countryRegion"
    #: Is signature present?.
    SIGNATURE = "signature"
    #: List of subfields of the same type.
    ARRAY = "array"
    #: Named list of subfields of potentially different types.
    OBJECT = "object"
    #: Currency amount with optional currency symbol and unit.
    CURRENCY = "currency"
    #: Parsed address.
    ADDRESS = "address"
    #: Boolean value, normalized to true or false.
    BOOLEAN = "boolean"

class DocumentFormulaKind(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Formula kind.
    """

    #: A formula embedded within the content of a paragraph.
    INLINE = "inline"
    #: A formula in display mode that takes up an entire line.
    DISPLAY = "display"

class DocumentSignatureType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Presence of signature.
    """

    #: A signature is detected.
    SIGNED = "signed"
    #: No signatures are detected.
    UNSIGNED = "unsigned"

class DocumentTableCellKind(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Table cell kind.
    """

    #: Contains the main content/data.
    CONTENT = "content"
    #: Describes the content of the row.
    ROW_HEADER = "rowHeader"
    #: Describes the content of the column.
    COLUMN_HEADER = "columnHeader"
    #: Describes the row headers, usually located at the top left corner of a table.
    STUB_HEAD = "stubHead"
    #: Describes the content in (parts of) the table.
    DESCRIPTION = "description"

class FontStyle(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Font style.
    """

    #: Characters are represented normally.
    NORMAL = "normal"
    #: Characters are visually slanted to the right.
    ITALIC = "italic"

class FontWeight(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Font weight.
    """

    #: Characters are represented normally.
    NORMAL = "normal"
    #: Characters are represented with thicker strokes.
    BOLD = "bold"

class LengthUnit(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The unit used by the width, height, and polygon properties. For images, the unit is "pixel".
    For PDF, the unit is "inch".
    """

    #: Length unit for image files.
    PIXEL = "pixel"
    #: Length unit for PDF files.
    INCH = "inch"

class OperationKind(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of operation.
    """

    #: Build a new custom document model.
    DOCUMENT_MODEL_BUILD = "documentModelBuild"
    #: Compose a new custom document model from existing models.
    DOCUMENT_MODEL_COMPOSE = "documentModelCompose"
    #: Copy an existing document model to potentially a different resource, region, or subscription.
    DOCUMENT_MODEL_COPY_TO = "documentModelCopyTo"
    #: Build a new custom classifier model.
    DOCUMENT_CLASSIFIER_BUILD = "documentClassifierBuild"

class OperationStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Operation status.
    """

    #: The operation has not started yet.
    NOT_STARTED = "notStarted"
    #: The operation is in progress.
    RUNNING = "running"
    #: The operation has failed.
    FAILED = "failed"
    #: The operation has succeeded.
    SUCCEEDED = "succeeded"
    #: The operation has been canceled.
    CANCELED = "canceled"

class ParagraphRole(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Semantic role of the paragraph.
    """

    #: Text near the top edge of the page.
    PAGE_HEADER = "pageHeader"
    #: Text near the bottom edge of the page.
    PAGE_FOOTER = "pageFooter"
    #: Page number.
    PAGE_NUMBER = "pageNumber"
    #: Top-level title describing the entire document.
    TITLE = "title"
    #: Sub heading describing a section of the document.
    SECTION_HEADING = "sectionHeading"
    #: A note usually placed after the main content on a page.
    FOOTNOTE = "footnote"
    #: A block of formulas, often with shared alignment.
    FORMULA_BLOCK = "formulaBlock"

class SelectionMarkState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """State of the selection mark.
    """

    #: The selection mark is selected, often indicated by a check ✓ or cross X inside the selection
    #: mark.
    SELECTED = "selected"
    #: The selection mark is not selected.
    UNSELECTED = "unselected"

class StringIndexType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Method used to compute string offset and length.
    """

    #: User-perceived display character, or grapheme cluster, as defined by Unicode 8.0.0.
    TEXT_ELEMENTS = "textElements"
    #: Character unit represented by a single unicode code point.  Used by Python 3.
    UNICODE_CODE_POINT = "unicodeCodePoint"
    #: Character unit represented by a 16-bit Unicode code unit.  Used by JavaScript, Java, and .NET.
    UTF16_CODE_UNIT = "utf16CodeUnit"
