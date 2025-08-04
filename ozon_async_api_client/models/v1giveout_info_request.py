from typing import *

from pydantic import BaseModel, Field


class V1giveoutInfoRequest(BaseModel):
    """
    None model
    """

    giveout_id: int = Field(alias="giveout_id")
