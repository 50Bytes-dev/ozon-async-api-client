from typing import *

from pydantic import BaseModel, Field

from .create_report_response_code_no_deadline import CreateReportResponseCodeNoDeadline


class CreateReportResponse(BaseModel):
    """
    object model
    """

    result: Optional[CreateReportResponseCodeNoDeadline] = Field(alias="result", default=None)
