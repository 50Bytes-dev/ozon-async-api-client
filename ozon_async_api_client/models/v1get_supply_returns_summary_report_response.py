from typing import *

from pydantic import BaseModel, Field

from .v1get_supply_returns_summary_report_response_row import V1getSupplyReturnsSummaryReportResponseRow


class V1getSupplyReturnsSummaryReportResponse(BaseModel):
    """
    None model
    """

    last_id: Optional[Union[str, int]] = Field(alias="last_id", default=None)

    returns_summary_report_rows: Optional[List[Optional[V1getSupplyReturnsSummaryReportResponseRow]]] = Field(
        alias="returns_summary_report_rows", default=None
    )
