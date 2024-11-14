# ------------------------------------
# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

"""
FILE: sample_agents_with_code_interpreter_file_attachment.py

DESCRIPTION:
    This sample demonstrates how to use agent operations with code interpreter through file attachment from
    the Azure Agents service using a synchronous client.

USAGE:
    python sample_agents_with_code_interpreter_file_attachment.py

    Before running the sample:

    pip install azure-ai-projects azure-identity

    Set this environment variables with your own values:
    PROJECT_CONNECTION_STRING - the Azure AI Project connection string, as found in your AI Studio Project.
"""

import os
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import CodeInterpreterTool, MessageAttachment
from azure.ai.projects.models import FilePurpose
from azure.identity import DefaultAzureCredential
from pathlib import Path

# Create an Azure AI Client from a connection string, copied from your AI Studio project.
# At the moment, it should be in the format "<HostName>;<AzureSubscriptionId>;<ResourceGroup>;<HubName>"
# Customer needs to login to Azure subscription via Azure CLI and set the environment variables

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(), conn_str=os.environ["PROJECT_CONNECTION_STRING"]
)

with project_client:

    # upload a file and wait for it to be processed
    file = project_client.agents.upload_file_and_poll(
        file_path="nifty_500_quarterly_results.csv", purpose=FilePurpose.AGENTS
    )
    print(f"Uploaded file, file ID: {file.id}")

    # [START create_agent_and_message_with_code_interpreter_file_attachment]
    # notice that CodeInterpreter must be enabled in the agent creation,
    # otherwise the agent will not be able to see the file attachment for code interpretation
    agent = project_client.agents.create_agent(
        model="gpt-4-1106-preview",
        name="my-assistant",
        instructions="You are helpful assistant",
        tools=CodeInterpreterTool().definitions,
    )
    print(f"Created agent, agent ID: {agent.id}")

    thread = project_client.agents.create_thread()
    print(f"Created thread, thread ID: {thread.id}")

    # create an attachment
    attachment = MessageAttachment(file_id=file.id, tools=CodeInterpreterTool().definitions)

    # create a message
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create bar chart in TRANSPORTATION sector for the operating profit from the uploaded csv file and provide file to me?",
        attachments=[attachment],
    )
    # [END create_agent_and_message_with_code_interpreter_file_attachment]
    print(f"Created message, message ID: {message.id}")

    run = project_client.agents.create_and_process_run(thread_id=thread.id, assistant_id=agent.id)
    print(f"Run finished with status: {run.status}")

    if run.status == "failed":
        # Check if you got "Rate limit is exceeded.", then you want to get more quota
        print(f"Run failed: {run.last_error}")

    project_client.agents.delete_file(file.id)
    print("Deleted file")

    messages = project_client.agents.get_messages(thread_id=thread.id)
    print(f"Messages: {messages}")

    last_msg = messages.get_last_text_message_by_sender("assistant")
    if last_msg:
        print(f"Last Message: {last_msg.text.value}")

    for image_content in messages.image_contents:
        print(f"Image File ID: {image_content.image_file.file_id}")
        file_name = f"{image_content.image_file.file_id}_image_file.png"
        project_client.agents.save_file(file_id=image_content.image_file.file_id, file_name=file_name)
        print(f"Saved image file to: {Path.cwd() / file_name}")

    for file_path_annotation in messages.file_path_annotations:
        print(f"File Paths:")
        print(f"Type: {file_path_annotation.type}")
        print(f"Text: {file_path_annotation.text}")
        print(f"File ID: {file_path_annotation.file_path.file_id}")
        print(f"Start Index: {file_path_annotation.start_index}")
        print(f"End Index: {file_path_annotation.end_index}")

    project_client.agents.delete_agent(agent.id)
    print("Deleted agent")
