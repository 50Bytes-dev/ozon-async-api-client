from typing import *

from pydantic import BaseModel, Field

from .compensation_report_language import CompensationReportLanguage


class V1getCompensationReportRequest(BaseModel):
    """
    None model
    """

    date: str = Field(alias="date")

    language: Optional[CompensationReportLanguage] = Field(alias="language", default=None)
