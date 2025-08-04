from typing import *

from pydantic import BaseModel, Field

from .get_realization_report_response_v2header import GetRealizationReportResponseV2header
from .v1get_realization_report_posting_response_row import V1getRealizationReportPostingResponseRow


class V1getRealizationReportPostingResponse(BaseModel):
    """
    object model

    Результат запроса.
    """

    header: Optional[GetRealizationReportResponseV2header] = Field(alias="header", default=None)

    rows: Optional[List[Optional[V1getRealizationReportPostingResponseRow]]] = Field(alias="rows", default=None)
