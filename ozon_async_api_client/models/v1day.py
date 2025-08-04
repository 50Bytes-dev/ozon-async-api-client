from typing import *

from pydantic import BaseModel, Field

from .v1day_time_slot import V1dayTimeSlot


class V1day(BaseModel):
    """
    None model
    """

    date_in_timezone: Optional[str] = Field(alias="date_in_timezone", default=None)

    timeslots: Optional[List[Optional[V1dayTimeSlot]]] = Field(alias="timeslots", default=None)
