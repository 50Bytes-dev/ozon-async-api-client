from typing import *

from pydantic import BaseModel, Field


class V2reportReturnsCreateRequestFilter(BaseModel):
    """
    object model

    Фильтр.
    """

    delivery_schema: Optional[str] = Field(alias="delivery_schema", default=None)

    date_from: str = Field(alias="date_from")

    date_to: str = Field(alias="date_to")

    status: str = Field(alias="status")
