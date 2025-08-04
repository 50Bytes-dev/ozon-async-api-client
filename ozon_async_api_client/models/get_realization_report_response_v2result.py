from typing import *

from pydantic import BaseModel, Field

from .get_realization_report_response_v2header import GetRealizationReportResponseV2header
from .get_realization_report_response_v2row import GetRealizationReportResponseV2row


class GetRealizationReportResponseV2result(BaseModel):
    """
    object model

    Результат запроса.
    """

    header: Optional[GetRealizationReportResponseV2header] = Field(alias="header", default=None)

    rows: Optional[List[Optional[GetRealizationReportResponseV2row]]] = Field(alias="rows", default=None)
