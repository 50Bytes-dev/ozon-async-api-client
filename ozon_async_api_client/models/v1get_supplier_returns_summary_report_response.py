from typing import *

from pydantic import BaseModel, Field

from .v1get_supplier_returns_summary_report_response_row import V1getSupplierReturnsSummaryReportResponseRow


class V1getSupplierReturnsSummaryReportResponse(BaseModel):
    """
    None model
    """

    last_id: Optional[Union[str, int]] = Field(alias="last_id", default=None)

    returns_summary_report_rows: Optional[List[Optional[V1getSupplierReturnsSummaryReportResponseRow]]] = Field(
        alias="returns_summary_report_rows", default=None
    )
