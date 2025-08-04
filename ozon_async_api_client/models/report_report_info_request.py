from typing import *

from pydantic import BaseModel, Field


class ReportReportInfoRequest(BaseModel):
    """
    ReportInfo model
    """

    code: Union[str, int] = Field(alias="code")
