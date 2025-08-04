from typing import *

from pydantic import BaseModel, Field


class V1supplyOrderTimeslot(BaseModel):
    """
    object model

    Время интервала поставки.
    """

    from_: str = Field(alias="from")

    to: str = Field(alias="to")
