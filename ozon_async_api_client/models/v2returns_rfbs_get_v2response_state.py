from typing import *

from pydantic import BaseModel, Field


class V2returnsRfbsGetV2responseState(BaseModel):
    """
    object model

    Данные о статусе возврата.
    """

    state: Optional[str] = Field(alias="state", default=None)

    state_name: Optional[str] = Field(alias="state_name", default=None)
