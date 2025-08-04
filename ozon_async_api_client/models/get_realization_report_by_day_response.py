from typing import *

from pydantic import BaseModel, Field

from .get_realization_report_by_day_response_row import GetRealizationReportByDayResponseRow


class GetRealizationReportByDayResponse(BaseModel):
    """
    object model

    Результат запроса.
    """

    rows: Optional[List[Optional[GetRealizationReportByDayResponseRow]]] = Field(alias="rows", default=None)
