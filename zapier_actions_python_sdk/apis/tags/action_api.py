# coding: utf-8

"""
    Zapier AI Actions API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from zapier_actions_python_sdk.paths.api_v1_exposed_exposed_app_action_id_execute.post import ExecuteAppAction
from zapier_actions_python_sdk.paths.api_v1_exposed.get import ListExposedActions
from zapier_actions_python_sdk.apis.tags.action_api_raw import ActionApiRaw


class ActionApi(
    ExecuteAppAction,
    ListExposedActions,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: ActionApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = ActionApiRaw(api_client)
