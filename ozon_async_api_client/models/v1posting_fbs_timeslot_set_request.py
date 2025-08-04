from typing import *

from pydantic import BaseModel, Field

from .v1posting_fbs_timeslot_set_new_timeslot import V1postingFbsTimeslotSetNewTimeslot


class V1postingFbsTimeslotSetRequest(BaseModel):
    """
    object model
    """

    new_timeslot: V1postingFbsTimeslotSetNewTimeslot = Field(alias="new_timeslot")

    posting_number: str = Field(alias="posting_number")
