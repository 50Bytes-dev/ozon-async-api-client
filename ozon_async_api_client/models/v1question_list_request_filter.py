from typing import *

from pydantic import BaseModel, Field


class V1questionListRequestFilter(BaseModel):
    """
    object model

    Фильтр.
    """

    date_from: Optional[str] = Field(alias="date_from", default=None)

    date_to: Optional[str] = Field(alias="date_to", default=None)

    status: Optional[str] = Field(alias="status", default=None)
