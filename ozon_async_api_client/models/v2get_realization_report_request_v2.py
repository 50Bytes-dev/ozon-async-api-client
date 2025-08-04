from typing import *

from pydantic import BaseModel, Field


class V2getRealizationReportRequestV2(BaseModel):
    """
    None model
    """

    month: int = Field(alias="month")

    year: int = Field(alias="year")
