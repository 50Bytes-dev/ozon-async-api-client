from typing import *

from pydantic import BaseModel, Field


class V1getRealizationReportByDayRequest(BaseModel):
    """
    None model
    """

    day: int = Field(alias="day")

    month: int = Field(alias="month")

    year: int = Field(alias="year")
