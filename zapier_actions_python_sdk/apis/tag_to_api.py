import typing_extensions

from zapier_actions_python_sdk.apis.tags import TagValues
from zapier_actions_python_sdk.apis.tags.action_api import ActionApi
from zapier_actions_python_sdk.apis.tags.check_api import CheckApi
from zapier_actions_python_sdk.apis.tags.configuration_api import ConfigurationApi
from zapier_actions_python_sdk.apis.tags.log_api import LogApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.ACTION: ActionApi,
        TagValues.CHECK: CheckApi,
        TagValues.CONFIGURATION: ConfigurationApi,
        TagValues.LOG: LogApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.ACTION: ActionApi,
        TagValues.CHECK: CheckApi,
        TagValues.CONFIGURATION: ConfigurationApi,
        TagValues.LOG: LogApi,
    }
)
