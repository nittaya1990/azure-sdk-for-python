# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
from promptflow._utils.async_utils import async_run_allowing_running_loop

from azure.ai.evaluation._common.constants import EvaluationMetrics

try:
    from ._content_safety_base import ContentSafetyEvaluatorBase
except ImportError:
    from _content_safety_base import ContentSafetyEvaluatorBase


class _AsyncSexualEvaluator(ContentSafetyEvaluatorBase):
    def __init__(self, azure_ai_project: dict, credential=None):
        super().__init__(
            metric=EvaluationMetrics.SEXUAL,
            azure_ai_project=azure_ai_project,
            credential=credential,
        )

    async def __call__(self, *, query: str, response: str, **kwargs):
        return await super().__call__(query=query, response=response, **kwargs)


class SexualEvaluator:
    """
    Initialize a sexual evaluator for sexual score.

    :param azure_ai_project: The scope of the Azure AI project.
        It contains subscription id, resource group, and project name.
    :type azure_ai_project: ~azure.ai.evaluation.AzureAIProject
    :param credential: The credential for connecting to Azure AI project.
    :type credential: ~azure.core.credentials.TokenCredential

    **Usage**

    .. code-block:: python

        azure_ai_project = {
            "subscription_id": "<subscription_id>",
            "resource_group_name": "<resource_group_name>",
            "project_name": "<project_name>",
        }
        eval_fn = SexualEvaluator(azure_ai_project)
        result = eval_fn(query="What is the capital of France?", response="Paris.")

    **Output format**

    .. code-block:: python

        {
            "sexual": "High",
            "sexual_score": 6.5,
            "sexual_reason": "Some reason"
        }
    """

    def __init__(self, azure_ai_project: dict, credential=None):
        self._async_evaluator = _AsyncSexualEvaluator(azure_ai_project, credential)

    def __call__(self, *, query: str, response: str, **kwargs):
        """
        Evaluates sexual content.

        :keyword query: The query to be evaluated.
        :paramtype query: str
        :keyword response: The response to be evaluated.
        :paramtype response: str
        :return: The sexual score.
        :rtype: dict
        """
        return async_run_allowing_running_loop(self._async_evaluator, query=query, response=response, **kwargs)

    def _to_async(self):
        return self._async_evaluator
