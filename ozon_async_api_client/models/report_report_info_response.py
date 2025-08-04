from typing import *

from pydantic import BaseModel, Field

from .report_reportinfo import ReportReportinfo


class ReportReportInfoResponse(BaseModel):
    """
    object model
    """

    result: Optional[ReportReportinfo] = Field(alias="result", default=None)
