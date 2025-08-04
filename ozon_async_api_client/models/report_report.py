from typing import *

from pydantic import BaseModel, Field


class ReportReport(BaseModel):
    """
    Common model

    Информация об отчёте.
    """

    code: Optional[str] = Field(alias="code", default=None)

    created_at: Optional[str] = Field(alias="created_at", default=None)

    error: Optional[str] = Field(alias="error", default=None)

    file: Optional[str] = Field(alias="file", default=None)

    params: Optional[Dict[str, Any]] = Field(alias="params", default=None)

    report_type: Optional[str] = Field(alias="report_type", default=None)

    status: Optional[str] = Field(alias="status", default=None)
