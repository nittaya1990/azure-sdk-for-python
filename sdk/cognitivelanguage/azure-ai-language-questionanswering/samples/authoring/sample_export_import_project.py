# coding=utf-8
# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

"""
FILE: sample_export_import_project.py

DESCRIPTION:
    This sample demonstrates how to export and import a Qna project.

USAGE:
    python sample_export_import_project.py

    Set the environment variables with your own values before running the sample:
    1) AZURE_QUESTIONANSWERING_ENDPOINT - the endpoint to your QuestionAnswering resource.
    2) AZURE_QUESTIONANSWERING_KEY - your QuestionAnswering API key.
    3) AZURE_QUESTIONANSWERING_PROJECT - your existing Question Answering project to export/import.
"""


def sample_export_import_project():
    # [START export_import_project]
    import os
    import io
    import zipfile
    from azure.core.rest import HttpRequest
    from azure.core.credentials import AzureKeyCredential
    from azure.ai.language.questionanswering.authoring import AuthoringClient

    # get service secrets
    endpoint = os.environ["AZURE_QUESTIONANSWERING_ENDPOINT"]
    key = os.environ["AZURE_QUESTIONANSWERING_KEY"]
    project_name = os.environ["AZURE_QUESTIONANSWERING_PROJECT"]

    # create client
    client = AuthoringClient(endpoint, AzureKeyCredential(key))
    with client:

        # export
        export_format = "json"
        export_poller = client.begin_export(
            project_name=project_name,
            file_format=export_format
        )
        export_result = export_poller.result()
        export_url = export_result["resultUrl"]
        request = HttpRequest("GET", export_url)
        exported_project = None

        if export_format == "json":
            response = client.send_request(request)
            exported_project = response.json()
        elif export_format == "excel" or export_format == "tsv":
            response = client.send_request(request, stream=True)
            exported_project = zipfile.ZipFile(io.BytesIO(response.read()))
            exported_project.extractall("./ExportedProject")
            exported_project.close()
            print(f"{export_format} project files written to ./ExportedProject.")
            return

        # import project
        import_poller = client.begin_import_assets(
            project_name=f"{project_name}-imported",
            options=exported_project,
        )
        import_poller.result()

        # list projects
        print("view all qna projects:")
        qna_projects = client.list_projects()
        for p in qna_projects:
            if p["projectName"] == project_name:
                print("project: {}".format(p["projectName"]))
                print("\tlanguage: {}".format(p["language"]))
                print("\tdescription: {}".format(p["description"]))

    # [END export_import_project]


if __name__ == '__main__':
    sample_export_import_project()
