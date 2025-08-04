from typing import *

from pydantic import BaseModel, Field

from .report_list_request_report_type import ReportListRequestReportType


class ReportReportListRequest(BaseModel):
    """
    ReportList model
    """

    page: int = Field(alias="page")

    page_size: int = Field(alias="page_size")

    report_type: Optional[ReportListRequestReportType] = Field(alias="report_type", default=None)
