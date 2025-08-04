from typing import *

from pydantic import BaseModel, Field

from .language_language import LanguageLanguage


class V1getAttributesRequest(BaseModel):
    """
    object model
    """

    description_category_id: int = Field(alias="description_category_id")

    language: Optional[LanguageLanguage] = Field(alias="language", default=None)

    type_id: int = Field(alias="type_id")
