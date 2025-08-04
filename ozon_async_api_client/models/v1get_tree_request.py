from typing import *

from pydantic import BaseModel, Field

from .language_language import LanguageLanguage


class V1getTreeRequest(BaseModel):
    """
    object model
    """

    language: Optional[LanguageLanguage] = Field(alias="language", default=None)
