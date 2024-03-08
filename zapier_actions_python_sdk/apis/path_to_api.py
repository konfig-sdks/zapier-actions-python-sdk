import typing_extensions

from zapier_actions_python_sdk.paths import PathValues
from zapier_actions_python_sdk.apis.paths.api_v1_check import ApiV1Check
from zapier_actions_python_sdk.apis.paths.api_v1_configuration_link import ApiV1ConfigurationLink
from zapier_actions_python_sdk.apis.paths.api_v1_exposed import ApiV1Exposed
from zapier_actions_python_sdk.apis.paths.api_v1_exposed_exposed_app_action_id_execute import ApiV1ExposedExposedAppActionIdExecute
from zapier_actions_python_sdk.apis.paths.api_v1_execution_log_execution_log_id import ApiV1ExecutionLogExecutionLogId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.API_V1_CHECK: ApiV1Check,
        PathValues.API_V1_CONFIGURATIONLINK: ApiV1ConfigurationLink,
        PathValues.API_V1_EXPOSED: ApiV1Exposed,
        PathValues.API_V1_EXPOSED_EXPOSED_APP_ACTION_ID_EXECUTE: ApiV1ExposedExposedAppActionIdExecute,
        PathValues.API_V1_EXECUTIONLOG_EXECUTION_LOG_ID: ApiV1ExecutionLogExecutionLogId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.API_V1_CHECK: ApiV1Check,
        PathValues.API_V1_CONFIGURATIONLINK: ApiV1ConfigurationLink,
        PathValues.API_V1_EXPOSED: ApiV1Exposed,
        PathValues.API_V1_EXPOSED_EXPOSED_APP_ACTION_ID_EXECUTE: ApiV1ExposedExposedAppActionIdExecute,
        PathValues.API_V1_EXECUTIONLOG_EXECUTION_LOG_ID: ApiV1ExecutionLogExecutionLogId,
    }
)
