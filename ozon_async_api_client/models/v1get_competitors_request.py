from typing import *

from pydantic import BaseModel, Field


class V1getCompetitorsRequest(BaseModel):
    """
    object model
    """

    page: int = Field(alias="page")

    limit: int = Field(alias="limit")
