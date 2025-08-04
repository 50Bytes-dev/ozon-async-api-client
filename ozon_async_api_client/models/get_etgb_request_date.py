from typing import *

from pydantic import BaseModel, Field


class GetEtgbRequestDate(BaseModel):
    """
    object model

    Фильтр по периоду создания деклараций.
    """

    from_: str = Field(alias="from")

    to: str = Field(alias="to")
