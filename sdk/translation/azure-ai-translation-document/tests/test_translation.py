# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

import functools
import pytest
import json
import os
from azure.core.exceptions import HttpResponseError
from testcase import DocumentTranslationTest, Document
from preparer import (
    DocumentTranslationPreparer,
    DocumentTranslationClientPreparer as _DocumentTranslationClientPreparer,
)
from devtools_testutils import recorded_by_proxy
from azure.storage.blob import ContainerClient
from azure.ai.translation.document.models._models import StartTranslationDetails as _StartTranslationDetails
from azure.ai.translation.document import (
    DocumentTranslationInput,
    TranslationTarget,
    TranslationGlossary,
)
from azure.ai.translation.document import DocumentTranslationClient

DocumentTranslationClientPreparer = functools.partial(_DocumentTranslationClientPreparer, DocumentTranslationClient)

GLOSSARY_FILE_NAME = os.path.abspath(os.path.join(os.path.abspath(__file__), "..", "./glossaries-valid.csv"))


class TestTranslation(DocumentTranslationTest):
    @pytest.mark.skip("Failing in PPE: https://github.com/Azure/azure-sdk-for-python/issues/26807")
    @pytest.mark.live_test_only
    @DocumentTranslationPreparer()
    def test_active_directory_auth(self, **kwargs):
        translation_document_test_endpoint = kwargs.pop("translation_document_test_endpoint")
        token = self.get_credential(DocumentTranslationClient)
        kwargs = {}
        if os.getenv("AZURE_COGNITIVE_SCOPE"):
            kwargs["credential_scopes"] = [os.getenv("AZURE_COGNITIVE_SCOPE")]
        client = DocumentTranslationClient(translation_document_test_endpoint, token, **kwargs)
        # prepare containers and test data
        blob_data = b"This is some text"
        source_container_sas_url = self.create_source_container(data=Document(data=blob_data))
        target_container_sas_url = self.create_target_container()

        # prepare translation inputs
        translation_inputs = [
            DocumentTranslationInput(
                source_url=source_container_sas_url,
                targets=[TranslationTarget(target_url=target_container_sas_url, language="fr")],
            )
        ]

        # submit translation and test
        self._begin_and_validate_translation(client, translation_inputs, 1, "fr")

    @DocumentTranslationPreparer()
    @DocumentTranslationClientPreparer()
    @recorded_by_proxy
    def test_single_source_single_target(self, **kwargs):
        client = kwargs.pop("client")
        variables = kwargs.pop("variables", {})
        # prepare containers and test data
        blob_data = b"This is some text"
        source_container_sas_url = self.create_source_container(data=Document(data=blob_data), variables=variables)
        target_container_sas_url = self.create_target_container(variables=variables)

        # prepare translation inputs
        translation_inputs = [
            DocumentTranslationInput(
                source_url=source_container_sas_url,
                targets=[TranslationTarget(target_url=target_container_sas_url, language="es")],
            )
        ]

        # submit translation and test
        self._begin_and_validate_translation(client, translation_inputs, 1, "es")
        return variables

    @DocumentTranslationPreparer()
    @DocumentTranslationClientPreparer()
    @recorded_by_proxy
    def test_single_source_two_targets(self, **kwargs):
        client = kwargs.pop("client")
        variables = kwargs.pop("variables", {})
        # prepare containers and test data
        blob_data = b"This is some text"
        source_container_sas_url = self.create_source_container(data=Document(data=blob_data), variables=variables)
        target_container_sas_url = self.create_target_container(variables=variables)
        additional_target_container_sas_url = self.create_target_container(variables=variables, container_suffix="2")

        # prepare translation inputs
        translation_inputs = [
            DocumentTranslationInput(
                source_url=source_container_sas_url,
                targets=[
                    TranslationTarget(target_url=target_container_sas_url, language="es"),
                    TranslationTarget(target_url=additional_target_container_sas_url, language="fr"),
                ],
            )
        ]

        # submit translation and test
        self._begin_and_validate_translation(client, translation_inputs, 2)
        return variables

    @DocumentTranslationPreparer()
    @DocumentTranslationClientPreparer()
    @recorded_by_proxy
    def test_multiple_sources_single_target(self, **kwargs):
        client = kwargs.pop("client")
        variables = kwargs.pop("variables", {})
        # prepare containers and test data
        blob_data = b"This is some text"
        source_container_sas_url = self.create_source_container(data=Document(data=blob_data), variables=variables)
        blob_data = b"This is some text2"
        additional_source_container_sas_url = self.create_source_container(
            data=Document(data=blob_data), variables=variables, container_suffix="2"
        )
        target_container_sas_url = self.create_target_container(variables=variables)

        # prepare translation inputs
        translation_inputs = [
            DocumentTranslationInput(
                source_url=source_container_sas_url,
                targets=[TranslationTarget(target_url=target_container_sas_url, language="es")],
            ),
            DocumentTranslationInput(
                source_url=additional_source_container_sas_url,
                targets=[TranslationTarget(target_url=target_container_sas_url, language="fr")],
            ),
        ]

        # submit translation and test
        self._begin_and_validate_translation(client, translation_inputs, 2)
        return variables

    @DocumentTranslationPreparer()
    @DocumentTranslationClientPreparer()
    @recorded_by_proxy
    def test_single_source_single_target_with_prefix(self, **kwargs):
        client = kwargs.pop("client")
        variables = kwargs.pop("variables", {})
        # prepare containers and test data
        blob_data = b"This is some text"
        prefix = "xyz"
        source_container_sas_url = self.create_source_container(
            data=Document(data=blob_data, prefix=prefix), variables=variables
        )
        target_container_sas_url = self.create_target_container(variables=variables)

        # prepare translation inputs
        translation_inputs = [
            DocumentTranslationInput(
                source_url=source_container_sas_url,
                targets=[TranslationTarget(target_url=target_container_sas_url, language="es")],
                prefix=prefix,
            )
        ]

        # submit translation and test
        self._begin_and_validate_translation(client, translation_inputs, 1, "es")
        return variables

    @DocumentTranslationPreparer()
    @DocumentTranslationClientPreparer()
    @recorded_by_proxy
    def test_single_source_single_target_with_suffix(self, **kwargs):
        client = kwargs.pop("client")
        variables = kwargs.pop("variables", {})
        # prepare containers and test data
        blob_data = b"This is some text"
        suffix = "txt"
        source_container_sas_url = self.create_source_container(data=Document(data=blob_data), variables=variables)
        target_container_sas_url = self.create_target_container(variables=variables)

        # prepare translation inputs
        translation_inputs = [
            DocumentTranslationInput(
                source_url=source_container_sas_url,
                targets=[TranslationTarget(target_url=target_container_sas_url, language="es")],
                suffix=suffix,
            )
        ]

        # submit translation and test
        self._begin_and_validate_translation(client, translation_inputs, 1, "es")
        return variables

    @DocumentTranslationPreparer()
    @DocumentTranslationClientPreparer()
    @recorded_by_proxy
    def test_bad_input_source(self, **kwargs):
        client = kwargs.pop("client")
        variables = kwargs.pop("variables", {})
        # prepare containers and test data
        target_container_sas_url = self.create_target_container(variables=variables)

        # prepare translation inputs
        translation_inputs = [
            DocumentTranslationInput(
                source_url="https://idont.ex.ist",
                targets=[TranslationTarget(target_url=target_container_sas_url, language="es")],
            )
        ]

        with pytest.raises(HttpResponseError) as e:
            poller = client.begin_translation(translation_inputs)
            result = poller.result()
        assert e.value.error.code == "InvalidDocumentAccessLevel"
        return variables

    @DocumentTranslationPreparer()
    @DocumentTranslationClientPreparer()
    @recorded_by_proxy
    def test_bad_input_target(self, **kwargs):
        client = kwargs.pop("client")
        variables = kwargs.pop("variables", {})
        # prepare containers and test data
        blob_data = b"This is some text"
        source_container_sas_url = self.create_source_container(data=Document(data=blob_data), variables=variables)

        # prepare translation inputs
        translation_inputs = [
            DocumentTranslationInput(
                source_url=source_container_sas_url,
                targets=[TranslationTarget(target_url="https://idont.ex.ist", language="es")],
            )
        ]

        with pytest.raises(HttpResponseError) as e:
            poller = client.begin_translation(translation_inputs)
            result = poller.result()
        assert e.value.error.code == "InvalidTargetDocumentAccessLevel"
        return variables

    @DocumentTranslationPreparer()
    @DocumentTranslationClientPreparer()
    @recorded_by_proxy
    def test_use_supported_and_unsupported_files(self, **kwargs):
        client = kwargs.pop("client")
        variables = kwargs.pop("variables", {})
        # prepare containers and test data
        source_container_sas_url = self.create_source_container(
            data=[Document(suffix=".txt"), Document(suffix=".jpg")], variables=variables
        )
        target_container_sas_url = self.create_target_container(variables=variables)

        # prepare translation inputs
        translation_inputs = [
            DocumentTranslationInput(
                source_url=source_container_sas_url,
                targets=[TranslationTarget(target_url=target_container_sas_url, language="es")],
            )
        ]

        poller = client.begin_translation(translation_inputs)
        result = poller.result()
        self._validate_translation_metadata(poller=poller, status="Succeeded", total=1, succeeded=1)
        for document in result:
            self._validate_doc_status(document, "es")
        return variables

    @pytest.mark.skip("Service now raises exception in this case. Need to follow-up")
    @DocumentTranslationPreparer()
    @DocumentTranslationClientPreparer()
    @recorded_by_proxy
    def test_existing_documents_in_target(self, **kwargs):
        client = kwargs.pop("client")
        variables = kwargs.pop("variables", {})
        # prepare containers and test data
        source_container_sas_url = self.create_source_container(data=Document(name="document"), variables=variables)
        target_container_sas_url = self.create_target_container(data=Document(name="document"), variables=variables)

        # prepare translation inputs
        translation_inputs = [
            DocumentTranslationInput(
                source_url=source_container_sas_url,
                targets=[TranslationTarget(target_url=target_container_sas_url, language="es")],
            )
        ]

        poller = client.begin_translation(translation_inputs)
        result = poller.result()
        self._validate_translation_metadata(poller, status="Failed", total=1, failed=1)

        for doc in result:
            assert doc.status == "Failed"
            assert doc.error.code == "TargetFileAlreadyExists"
        return variables

    @pytest.mark.skip("Service now raises exception in this case. Need to follow-up")
    @DocumentTranslationPreparer()
    @DocumentTranslationClientPreparer()
    @recorded_by_proxy
    def test_existing_documents_in_target_one_valid(self, **kwargs):
        client = kwargs.pop("client")
        variables = kwargs.pop("variables", {})
        # prepare containers and test data
        source_container_sas_url = self.create_source_container(
            data=[Document(name="document"), Document()], variables=variables
        )
        target_container_sas_url = self.create_target_container(data=Document(name="document"), variables=variables)

        # prepare translation inputs
        translation_inputs = [
            DocumentTranslationInput(
                source_url=source_container_sas_url,
                targets=[TranslationTarget(target_url=target_container_sas_url, language="es")],
            )
        ]

        poller = client.begin_translation(translation_inputs)
        result = poller.result()
        self._validate_translation_metadata(poller, status="Succeeded", total=2, failed=1)

        for doc in result:
            if doc.status == "Failed":
                assert doc.error.code == "TargetFileAlreadyExists"
        return variables

    @DocumentTranslationPreparer()
    @DocumentTranslationClientPreparer()
    @recorded_by_proxy
    def test_empty_document(self, **kwargs):
        client = kwargs.pop("client")
        variables = kwargs.pop("variables", {})
        # prepare containers and test data
        source_container_sas_url = self.create_source_container(Document(data=b""), variables=variables)
        target_container_sas_url = self.create_target_container(variables=variables)

        # prepare translation inputs
        translation_inputs = [
            DocumentTranslationInput(
                source_url=source_container_sas_url,
                targets=[TranslationTarget(target_url=target_container_sas_url, language="es")],
            )
        ]

        poller = client.begin_translation(translation_inputs)
        result = poller.result()
        self._validate_translation_metadata(poller, status="Failed", total=1, failed=1)

        for doc in result:
            assert doc.status == "Failed"
            assert doc.error.code == "NoTranslatableText"
        return variables

    @DocumentTranslationPreparer()
    @DocumentTranslationClientPreparer()
    @recorded_by_proxy
    def test_overloaded_inputs(self, **kwargs):
        client = kwargs.pop("client")
        variables = kwargs.pop("variables", {})
        # prepare containers and test data
        source_container_sas_url = self.create_source_container(data=Document(data=b"hello world"), variables=variables)
        target_container_sas_url = self.create_target_container(variables=variables)
        target_container_sas_url_2 = self.create_target_container(variables=variables, container_suffix="2")

        # prepare translation inputs
        translation_inputs = [
            DocumentTranslationInput(
                source_url=source_container_sas_url,
                targets=[TranslationTarget(target_url=target_container_sas_url, language="es")],
            )
        ]

        # positional
        poller = client.begin_translation(translation_inputs)
        result = poller.result()
        self._validate_translation_metadata(poller, status="Succeeded", total=1, succeeded=1)

        # keyword
        translation_inputs[0].targets[0].target_url = target_container_sas_url_2
        poller = client.begin_translation(inputs=translation_inputs)
        result = poller.result()
        self._validate_translation_metadata(poller, status="Succeeded", total=1, succeeded=1)
        return variables

    @DocumentTranslationPreparer()
    @DocumentTranslationClientPreparer()
    @recorded_by_proxy
    def test_overloaded_single_input(self, **kwargs):
        client = kwargs.pop("client")
        variables = kwargs.pop("variables", {})
        # prepare containers and test data
        source_container_sas_url = self.create_source_container(data=Document(data=b"hello world"), variables=variables)
        target_container_sas_url = self.create_target_container(variables=variables)
        target_container_sas_url_2 = self.create_target_container(variables=variables, container_suffix="2")

        # positional
        poller = client.begin_translation(source_container_sas_url, target_container_sas_url, "es")
        result = poller.result()
        self._validate_translation_metadata(poller, status="Succeeded", total=1, succeeded=1)

        # keyword
        poller = client.begin_translation(
            source_url=source_container_sas_url, target_url=target_container_sas_url_2, target_language="es"
        )
        result = poller.result()
        self._validate_translation_metadata(poller, status="Succeeded", total=1, succeeded=1)
        return variables

    @DocumentTranslationPreparer()
    @DocumentTranslationClientPreparer()
    def test_overloaded_bad_input(self, **kwargs):
        client = kwargs.pop("client")
        translation_inputs = [
            DocumentTranslationInput(
                source_url="container", targets=[TranslationTarget(target_url="container", language="es")]
            )
        ]

        with pytest.raises(ValueError):
            client.begin_translation("container")

        with pytest.raises(ValueError):
            client.begin_translation("container", "container")

        with pytest.raises(ValueError):
            client.begin_translation(source_url=translation_inputs)

        with pytest.raises(ValueError):
            client.begin_translation(inputs="container")

    @pytest.mark.live_test_only
    @DocumentTranslationPreparer()
    @DocumentTranslationClientPreparer()
    def test_translation_continuation_token(self, **kwargs):
        client = kwargs.pop("client")
        source_container_sas_url = self.create_source_container(data=Document(data=b"hello world"))
        target_container_sas_url = self.create_target_container()

        initial_poller = client.begin_translation(source_container_sas_url, target_container_sas_url, "es")
        cont_token = initial_poller.continuation_token()

        poller = client.begin_translation(None, continuation_token=cont_token)
        result = poller.result()
        self._validate_translation_metadata(poller, status="Succeeded", total=1, succeeded=1)
        for doc in result:
            self._validate_doc_status(doc, target_language="es")
        initial_poller.wait()  # necessary so devtools_testutils doesn't throw assertion error

    @DocumentTranslationPreparer()
    @DocumentTranslationClientPreparer()
    @recorded_by_proxy
    def test_single_input_with_kwargs(self, **kwargs):
        client = kwargs.pop("client")
        variables = kwargs.pop("variables", {})
        # prepare containers and test data
        source_container_sas_url = self.create_source_container(data=Document(data=b"hello world"), variables=variables)
        target_container_sas_url = self.create_target_container(variables=variables)

        def callback(request):
            req = _StartTranslationDetails._deserialize(json.loads(request.http_request.body), [])
            input = req.inputs[0]
            assert input.source.source_url == source_container_sas_url
            assert input.source.language == "en"
            assert input.source.filter.prefix == ""
            assert input.source.filter.suffix == ".txt"
            assert input.storage_type == "File"
            assert input.targets[0].category_id == "fake"
            assert input.targets[0].glossaries[0].file_format == "txt"
            assert input.targets[0].glossaries[0].glossary_url == "https://glossaryfile.txt"
            assert input.targets[0].language == "es"
            assert input.targets[0].target_url == target_container_sas_url

        try:
            poller = client.begin_translation(
                source_container_sas_url,
                target_container_sas_url,
                "es",
                storage_type="File",
                source_language="en",
                prefix="",
                suffix=".txt",
                category_id="fake",
                glossaries=[TranslationGlossary(glossary_url="https://glossaryfile.txt", file_format="txt")],
                raw_response_hook=callback,
            )
            poller.result()
        except HttpResponseError as e:
            pass
        return variables

    @DocumentTranslationPreparer()
    @DocumentTranslationClientPreparer()
    @recorded_by_proxy
    def test_single_input_with_kwarg_successful(self, **kwargs):
        client = kwargs.pop("client")
        variables = kwargs.pop("variables", {})
        # prepare containers and test data
        source_container_sas_url = self.create_source_container(
            data=[Document(data=b"hello world", prefix="kwargs"), Document(data=b"hello world")], variables=variables
        )
        target_container_sas_url = self.create_target_container(variables=variables)

        poller = client.begin_translation(source_container_sas_url, target_container_sas_url, "fr", prefix="kwargs")
        result = poller.result()
        self._validate_translation_metadata(poller, status="Succeeded", total=1, succeeded=1)
        for doc in result:
            self._validate_doc_status(doc, target_language="fr")
        return variables

    @pytest.mark.skip("Flaky test")
    @pytest.mark.live_test_only
    @DocumentTranslationPreparer()
    @DocumentTranslationClientPreparer()
    def test_translation_with_glossary(self, **kwargs):
        client = kwargs.pop("client")
        doc = Document(data=b"testing")
        source_container_sas_url = self.create_source_container(data=[doc])
        target_container_sas_url = self.create_target_container()

        container_client = ContainerClient(self.storage_endpoint, self.source_container_name, self.storage_key)
        with open(GLOSSARY_FILE_NAME, "rb") as fd:
            container_client.upload_blob(name=GLOSSARY_FILE_NAME, data=fd.read())

        prefix, suffix = source_container_sas_url.split("?")
        glossary_file_sas_url = prefix + "/" + GLOSSARY_FILE_NAME + "?" + suffix

        poller = client.begin_translation(
            source_container_sas_url,
            target_container_sas_url,
            "es",
            glossaries=[TranslationGlossary(glossary_url=glossary_file_sas_url, file_format="csv")],
        )
        result = poller.result()

        container_client = ContainerClient(self.storage_endpoint, self.target_container_name, self.storage_key)

        # download translated file and assert that translation reflects glossary changes
        document = doc.name + doc.suffix
        with open(document, "wb") as my_blob:
            download_stream = container_client.download_blob(document)
            my_blob.write(download_stream.readall())

        with open(document, "rb") as fd:
            translated = fd.readline()

        assert b"essai" in translated  # glossary worked
        os.remove(document)
