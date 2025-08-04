from typing import *

from pydantic import BaseModel, Field


class V1draftTimeslotInfoRequest(BaseModel):
    """
    DraftTimeslotInfo messages model
    """

    date_from: str = Field(alias="date_from")

    date_to: str = Field(alias="date_to")

    draft_id: int = Field(alias="draft_id")

    warehouse_ids: List[int] = Field(alias="warehouse_ids")
