from typing import *

from pydantic import BaseModel, Field

from .error_error_level import ErrorErrorLevel
from .error_human_texts import ErrorHumanTexts


class GetProductInfoListResponseError(BaseModel):
    """
    object model
    """

    attribute_id: Optional[int] = Field(alias="attribute_id", default=None)

    code: Optional[str] = Field(alias="code", default=None)

    field: Optional[str] = Field(alias="field", default=None)

    level: Optional[ErrorErrorLevel] = Field(alias="level", default=None)

    state: Optional[str] = Field(alias="state", default=None)

    texts: Optional[ErrorHumanTexts] = Field(alias="texts", default=None)
