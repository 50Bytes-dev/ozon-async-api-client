from typing import *

from pydantic import BaseModel, Field

from .human_texts_param import HumanTextsParam


class ErrorHumanTexts(BaseModel):
    """
    object model

    Описание ошибок.
    """

    attribute_name: Optional[str] = Field(alias="attribute_name", default=None)

    description: Optional[str] = Field(alias="description", default=None)

    hint_code: Optional[str] = Field(alias="hint_code", default=None)

    message: Optional[str] = Field(alias="message", default=None)

    params: Optional[List[Optional[HumanTextsParam]]] = Field(alias="params", default=None)

    short_description: Optional[str] = Field(alias="short_description", default=None)
