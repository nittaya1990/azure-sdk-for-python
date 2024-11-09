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

from msrest.serialization import Model


class RankableAction(Model):
    """An action with it's associated features used for ranking.

    All required parameters must be populated in order to send to Azure.

    :param id: Required. Id of the action.
    :type id: str
    :param features: Required. List of dictionaries containing features.
    :type features: list[object]
    """

    _validation = {
        "id": {"required": True, "max_length": 256},
        "features": {"required": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "features": {"key": "features", "type": "[object]"},
    }

    def __init__(self, **kwargs):
        super(RankableAction, self).__init__(**kwargs)
        self.id = kwargs.get("id", None)
        self.features = kwargs.get("features", None)
