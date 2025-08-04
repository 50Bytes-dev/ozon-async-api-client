from typing import *

from pydantic import BaseModel, Field


class ReturnsRfbsGetV2responseClientReturnMethodType(BaseModel):
    """
    object model

    Данные о способе возврата.
    """

    id: Optional[int] = Field(alias="id", default=None)

    name: Optional[str] = Field(alias="name", default=None)
