# coding: utf-8

"""
    Zapier AI Actions API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from zapier_actions_python_sdk import schemas  # noqa: F401


class ExecuteResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    This is a summary of the results given the action that was executed.
    """


    class MetaOapg:
        required = {
            "action_used",
            "input_params",
            "review_url",
            "id",
            "additional_results",
        }
        
        class properties:
            id = schemas.StrSchema
            action_used = schemas.StrSchema
            input_params = schemas.DictSchema
            review_url = schemas.StrSchema
        
            @staticmethod
            def additional_results() -> typing.Type['ExecuteResponseAdditionalResults']:
                return ExecuteResponseAdditionalResults
            result = schemas.DictSchema
            result_field_labels = schemas.DictSchema
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "success": "SUCCESS",
                        "error": "ERROR",
                        "empty": "EMPTY",
                        "preview": "PREVIEW",
                    }
                
                @schemas.classproperty
                def SUCCESS(cls):
                    return cls("success")
                
                @schemas.classproperty
                def ERROR(cls):
                    return cls("error")
                
                @schemas.classproperty
                def EMPTY(cls):
                    return cls("empty")
                
                @schemas.classproperty
                def PREVIEW(cls):
                    return cls("preview")
            error = schemas.StrSchema
            assistant_hint = schemas.StrSchema
            __annotations__ = {
                "id": id,
                "action_used": action_used,
                "input_params": input_params,
                "review_url": review_url,
                "additional_results": additional_results,
                "result": result,
                "result_field_labels": result_field_labels,
                "status": status,
                "error": error,
                "assistant_hint": assistant_hint,
            }
    
    action_used: MetaOapg.properties.action_used
    input_params: MetaOapg.properties.input_params
    review_url: MetaOapg.properties.review_url
    id: MetaOapg.properties.id
    additional_results: 'ExecuteResponseAdditionalResults'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["action_used"]) -> MetaOapg.properties.action_used: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["input_params"]) -> MetaOapg.properties.input_params: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["review_url"]) -> MetaOapg.properties.review_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["additional_results"]) -> 'ExecuteResponseAdditionalResults': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["result"]) -> MetaOapg.properties.result: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["result_field_labels"]) -> MetaOapg.properties.result_field_labels: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["error"]) -> MetaOapg.properties.error: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["assistant_hint"]) -> MetaOapg.properties.assistant_hint: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "action_used", "input_params", "review_url", "additional_results", "result", "result_field_labels", "status", "error", "assistant_hint", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["action_used"]) -> MetaOapg.properties.action_used: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["input_params"]) -> MetaOapg.properties.input_params: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["review_url"]) -> MetaOapg.properties.review_url: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["additional_results"]) -> 'ExecuteResponseAdditionalResults': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["result"]) -> typing.Union[MetaOapg.properties.result, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["result_field_labels"]) -> typing.Union[MetaOapg.properties.result_field_labels, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["error"]) -> typing.Union[MetaOapg.properties.error, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["assistant_hint"]) -> typing.Union[MetaOapg.properties.assistant_hint, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "action_used", "input_params", "review_url", "additional_results", "result", "result_field_labels", "status", "error", "assistant_hint", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        action_used: typing.Union[MetaOapg.properties.action_used, str, ],
        input_params: typing.Union[MetaOapg.properties.input_params, dict, frozendict.frozendict, ],
        review_url: typing.Union[MetaOapg.properties.review_url, str, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        additional_results: 'ExecuteResponseAdditionalResults',
        result: typing.Union[MetaOapg.properties.result, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        result_field_labels: typing.Union[MetaOapg.properties.result_field_labels, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        error: typing.Union[MetaOapg.properties.error, str, schemas.Unset] = schemas.unset,
        assistant_hint: typing.Union[MetaOapg.properties.assistant_hint, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ExecuteResponse':
        return super().__new__(
            cls,
            *args,
            action_used=action_used,
            input_params=input_params,
            review_url=review_url,
            id=id,
            additional_results=additional_results,
            result=result,
            result_field_labels=result_field_labels,
            status=status,
            error=error,
            assistant_hint=assistant_hint,
            _configuration=_configuration,
            **kwargs,
        )

from zapier_actions_python_sdk.model.execute_response_additional_results import ExecuteResponseAdditionalResults
