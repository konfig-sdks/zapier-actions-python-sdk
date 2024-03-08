# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from zapier_actions_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    ACTION = "Action"
    CHECK = "Check"
    CONFIGURATION = "Configuration"
    LOG = "Log"