<div align=>

[![Visit Zapier](./header.png)](https://zapier.com)

# Zapier<a id="zapier"></a>

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`zapieractions.action.execute_app_action`](#zapieractionsactionexecute_app_action)
  * [`zapieractions.action.list_exposed_actions`](#zapieractionsactionlist_exposed_actions)
  * [`zapieractions.check.auth_test_get`](#zapieractionscheckauth_test_get)
  * [`zapieractions.configuration.get_configuration_link`](#zapieractionsconfigurationget_configuration_link)
  * [`zapieractions.log.get_execution_log`](#zapieractionslogget_execution_log)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Zapier&serviceName=AI%20Actions&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from zapier_actions_python_sdk import ZapierActions, ApiException

zapieractions = ZapierActions(

        access_point_api_key_header = 'YOUR_API_KEY',

        access_point_api_key_query = 'YOUR_API_KEY',

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',,

        session_auth = 'YOUR_API_KEY',
)

try:
    # Execute App Action Endpoint
    execute_app_action_response = zapieractions.action.execute_app_action(
        instructions="string_example",
        exposed_app_action_id="01ARZ3NDEKTSV4RRFFQ69G5FAV",
        preview_only=False,
    )
    print(execute_app_action_response)
except ApiException as e:
    print("Exception when calling ActionApi.execute_app_action: %s\n" % e)
    pprint(e.body)
    if e.status == 400:
        pprint(e.body["error"])
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python

import asyncio
from pprint import pprint
from zapier_actions_python_sdk import ZapierActions, ApiException

zapieractions = ZapierActions(

        access_point_api_key_header = 'YOUR_API_KEY',

        access_point_api_key_query = 'YOUR_API_KEY',

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',,

        session_auth = 'YOUR_API_KEY',
)

async def main():
    try:
        # Execute App Action Endpoint
        execute_app_action_response = await zapieractions.action.aexecute_app_action(
            instructions="string_example",
            exposed_app_action_id="01ARZ3NDEKTSV4RRFFQ69G5FAV",
            preview_only=False,
        )
        print(execute_app_action_response)
    except ApiException as e:
        print("Exception when calling ActionApi.execute_app_action: %s\n" % e)
        pprint(e.body)
        if e.status == 400:
            pprint(e.body["error"])
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)

asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from zapier_actions_python_sdk import ZapierActions, ApiException

zapieractions = ZapierActions(

        access_point_api_key_header = 'YOUR_API_KEY',

        access_point_api_key_query = 'YOUR_API_KEY',

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',,

        session_auth = 'YOUR_API_KEY',
)

try:
    # Execute App Action Endpoint
    execute_app_action_response = zapieractions.action.raw.execute_app_action(
        instructions="string_example",
        exposed_app_action_id="01ARZ3NDEKTSV4RRFFQ69G5FAV",
        preview_only=False,
    )
    pprint(execute_app_action_response.body)
    pprint(execute_app_action_response.body["id"])
    pprint(execute_app_action_response.body["action_used"])
    pprint(execute_app_action_response.body["input_params"])
    pprint(execute_app_action_response.body["review_url"])
    pprint(execute_app_action_response.body["additional_results"])
    pprint(execute_app_action_response.body["result"])
    pprint(execute_app_action_response.body["result_field_labels"])
    pprint(execute_app_action_response.body["status"])
    pprint(execute_app_action_response.body["error"])
    pprint(execute_app_action_response.body["assistant_hint"])
    pprint(execute_app_action_response.headers)
    pprint(execute_app_action_response.status)
    pprint(execute_app_action_response.round_trip_time)
except ApiException as e:
    print("Exception when calling ActionApi.execute_app_action: %s\n" % e)
    pprint(e.body)
    if e.status == 400:
        pprint(e.body["error"])
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `zapieractions.action.execute_app_action`<a id="zapieractionsactionexecute_app_action"></a>

Give us a plain english description of exact action you want to do. There should be dynamically generated documentation for this endpoint for each action that is exposed.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
execute_app_action_response = zapieractions.action.execute_app_action(
    instructions="string_example",
    exposed_app_action_id="01ARZ3NDEKTSV4RRFFQ69G5FAV",
    preview_only=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### instructions: `str`<a id="instructions-str"></a>

Plain english instructions. Provide as much detail as possible, even if other fields are present.

##### exposed_app_action_id: `str`<a id="exposed_app_action_id-str"></a>

##### preview_only: `bool`<a id="preview_only-bool"></a>

If true, we will not execute the action, but will return the params of the preview.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ExecuteRequest`](./zapier_actions_python_sdk/type/execute_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ExecuteResponse`](./zapier_actions_python_sdk/pydantic/execute_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/exposed/{exposed_app_action_id}/execute` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zapieractions.action.list_exposed_actions`<a id="zapieractionsactionlist_exposed_actions"></a>

List all the currently exposed actions for the given account.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_exposed_actions_response = zapieractions.action.list_exposed_actions()
```

#### 🔄 Return<a id="🔄-return"></a>

[`ExposedActionResponseSchema`](./zapier_actions_python_sdk/pydantic/exposed_action_response_schema.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/exposed` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zapieractions.check.auth_test_get`<a id="zapieractionscheckauth_test_get"></a>

Test that the API and auth are working.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
zapieractions.check.auth_test_get()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/check` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zapieractions.configuration.get_configuration_link`<a id="zapieractionsconfigurationget_configuration_link"></a>

Provides a link to configure more actions. Alternatively, searching through apps and actions will provide more specific configuration links.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
zapieractions.configuration.get_configuration_link()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/configuration-link` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zapieractions.log.get_execution_log`<a id="zapieractionslogget_execution_log"></a>

Get the execution log for a given execution log id.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_execution_log_response = zapieractions.log.get_execution_log(
    execution_log_id="01ARZ3NDEKTSV4RRFFQ69G5FAV",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### execution_log_id: `str`<a id="execution_log_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`ExecuteResponse`](./zapier_actions_python_sdk/pydantic/execute_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/execution-log/{execution_log_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)