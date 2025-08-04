from typing import *

from pydantic import BaseModel, Field


class V1postingFbsTimeslotSetNewTimeslot(BaseModel):
    """
    object model

    Новый период для даты доставки.
    """

    from_: str = Field(alias="from")

    to: str = Field(alias="to")
