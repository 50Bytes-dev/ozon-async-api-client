from typing import *

from pydantic import BaseModel, Field


class V2timeslotZonedMessage(BaseModel):
    """
    object model
    """

    timeslot: Optional[Any] = Field(alias="timeslot", default=None)

    timezone_info: Optional[Any] = Field(alias="timezone_info", default=None)
