from typing import *

from pydantic import BaseModel, Field

from .v1day_time_slot import V1dayTimeSlot


class V1draftSupplyCreateRequest(BaseModel):
    """
    DraftSupplyCreate model
    """

    draft_id: int = Field(alias="draft_id")

    timeslot: Optional[V1dayTimeSlot] = Field(alias="timeslot", default=None)

    warehouse_id: int = Field(alias="warehouse_id")
