# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

import unittest

from azure.cognitiveservices.search.videosearch import VideoSearchClient
from msrest.authentication import CognitiveServicesCredentials

from devtools_testutils import AzureRecordedTestCase, AzureTestError
from devtools_testutils import mgmt_settings_fake as fake_settings


class VideoSearchTest(AzureRecordedTestCase):
    #FILTER_HEADERS = ReplayableTest.FILTER_HEADERS + ['Ocp-Apim-Subscription-Key']

    def __init__(self, method_name):
        self._fake_settings, self._real_settings = self._load_settings()
        super(VideoSearchTest, self).__init__(method_name)

    @property
    def settings(self):
        if self.is_live:
            if self._real_settings:
                return self._real_settings
            else:
                raise AzureTestError('Need a mgmt_settings_real.py file to run tests live.')
        else:
            return self._fake_settings

    def _load_settings(self):
        try:
            from devtools_testutils import mgmt_settings_real as real_settings
            return fake_settings, real_settings
        except ImportError:
            return fake_settings, None

    def test_search(self):
        raise unittest.SkipTest("Skipping test_search")
        credentials = CognitiveServicesCredentials(
            self.settings.CS_SUBSCRIPTION_KEY
        )
        video_search_api = VideoSearchClient(credentials)

        # FIXME
