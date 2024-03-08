# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from zapier_actions_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    API_V1_CHECK = "/api/v1/check"
    API_V1_CONFIGURATIONLINK = "/api/v1/configuration-link"
    API_V1_EXPOSED = "/api/v1/exposed"
    API_V1_EXPOSED_EXPOSED_APP_ACTION_ID_EXECUTE = "/api/v1/exposed/{exposed_app_action_id}/execute"
    API_V1_EXECUTIONLOG_EXECUTION_LOG_ID = "/api/v1/execution-log/{execution_log_id}"
