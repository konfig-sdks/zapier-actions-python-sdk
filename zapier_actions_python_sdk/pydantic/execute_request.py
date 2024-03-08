# coding: utf-8

"""
    Zapier AI Actions API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel


class ExecuteRequest(BaseModel):
    # Plain english instructions. Provide as much detail as possible, even if other fields are present.
    instructions: str = Field(alias='instructions')

    # If true, we will not execute the action, but will return the params of the preview.
    preview_only: typing.Optional[bool] = Field(None, alias='preview_only')
    class Config:
        arbitrary_types_allowed = True