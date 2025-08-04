from typing import *

from pydantic import BaseModel, Field

from .create_report_response_code import CreateReportResponseCode


class ReportCreateReportResponse(BaseModel):
    """
    object model
    """

    result: Optional[CreateReportResponseCode] = Field(alias="result", default=None)
