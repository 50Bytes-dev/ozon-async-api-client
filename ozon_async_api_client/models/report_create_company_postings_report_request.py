from typing import *

from pydantic import BaseModel, Field

from .report_create_company_postings_report_request_filter import ReportCreateCompanyPostingsReportRequestFilter
from .report_language import ReportLanguage


class ReportCreateCompanyPostingsReportRequest(BaseModel):
    """
    object model
    """

    filter: ReportCreateCompanyPostingsReportRequestFilter = Field(alias="filter")

    language: Optional[ReportLanguage] = Field(alias="language", default=None)
