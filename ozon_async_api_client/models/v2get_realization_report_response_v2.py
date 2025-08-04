from typing import *

from pydantic import BaseModel, Field

from .get_realization_report_response_v2result import GetRealizationReportResponseV2result


class V2getRealizationReportResponseV2(BaseModel):
    """
    None model
    """

    result: Optional[GetRealizationReportResponseV2result] = Field(alias="result", default=None)
