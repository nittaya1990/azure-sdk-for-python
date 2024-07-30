# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

"""
FILE: convert_windows_timezone_to_iana_async.py
DESCRIPTION:
    This API returns a corresponding IANA ID, given a valid Windows Time Zone ID.
USAGE:
    python convert_windows_timezone_to_iana_async.py

    Set the environment variables with your own values before running the sample:
    - AZURE_SUBSCRIPTION_KEY - your subscription key
"""
import asyncio
import os

from azure.core.exceptions import HttpResponseError

subscription_key = os.getenv("AZURE_SUBSCRIPTION_KEY", "your subscription key")

async def convert_windows_timezone_to_iana_async():
    from azure.core.credentials import AzureKeyCredential
    from azure.maps.timezone.aio import TimezoneClient

    timezone_client = TimezoneClient(credential=AzureKeyCredential(subscription_key))
    try:
        async with timezone_client:
            result = await timezone_client.convert_windows_timezone_to_iana(windows_timezone_id="Pacific Standard Time")
            print(result)
    except HttpResponseError as exception:
        if exception.error is not None:
            print(f"Error Code: {exception.error.code}")
            print(f"Message: {exception.error.message}")

if __name__ == '__main__':
    asyncio.run(convert_windows_timezone_to_iana_async())
