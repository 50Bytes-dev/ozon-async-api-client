from typing import *

from pydantic import BaseModel, Field

from .language_language import LanguageLanguage


class V1getAttributeValuesRequest(BaseModel):
    """
    object model
    """

    attribute_id: int = Field(alias="attribute_id")

    description_category_id: int = Field(alias="description_category_id")

    language: Optional[LanguageLanguage] = Field(alias="language", default=None)

    last_value_id: Optional[int] = Field(alias="last_value_id", default=None)

    limit: int = Field(alias="limit")

    type_id: int = Field(alias="type_id")
