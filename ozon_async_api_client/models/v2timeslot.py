from typing import *

from pydantic import BaseModel, Field


class V2timeslot(BaseModel):
    """
    object model
    """

    from_: Optional[str] = Field(alias="from", default=None)

    to: Optional[str] = Field(alias="to", default=None)
