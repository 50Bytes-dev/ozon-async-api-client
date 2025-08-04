from typing import *

from pydantic import BaseModel, Field


class GetCompetitorsResponseCompetitorInfo(BaseModel):
    """
    object model
    """

    name: Optional[str] = Field(alias="name", default=None)

    id: Optional[int] = Field(alias="id", default=None)
