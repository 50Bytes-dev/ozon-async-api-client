from typing import *

from pydantic import BaseModel, Field

from .report_list_response_result import ReportListResponseResult


class ReportReportListResponse(BaseModel):
    """
    object model
    """

    result: Optional[ReportListResponseResult] = Field(alias="result", default=None)
