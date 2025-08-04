from typing import *

from pydantic import BaseModel, Field

from .report_report import ReportReport


class ReportListResponseResult(BaseModel):
    """
    object model

    Результаты запроса.
    """

    reports: Optional[List[Optional[ReportReport]]] = Field(alias="reports", default=None)

    total: Optional[int] = Field(alias="total", default=None)
