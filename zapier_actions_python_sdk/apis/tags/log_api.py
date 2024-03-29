# coding: utf-8

"""
    Zapier AI Actions API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from zapier_actions_python_sdk.paths.api_v1_execution_log_execution_log_id.get import GetExecutionLog
from zapier_actions_python_sdk.apis.tags.log_api_raw import LogApiRaw


class LogApi(
    GetExecutionLog,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: LogApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = LogApiRaw(api_client)
