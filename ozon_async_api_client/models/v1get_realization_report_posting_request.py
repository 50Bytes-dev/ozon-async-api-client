from typing import *

from pydantic import BaseModel, Field


class V1getRealizationReportPostingRequest(BaseModel):
    """
    None model
    """

    month: int = Field(alias="month")

    year: int = Field(alias="year")
