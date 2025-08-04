from typing import *

from pydantic import BaseModel, Field

from .v3finance_cash_flow_statement_list_response_result import V3financeCashFlowStatementListResponseResult


class V3financeCashFlowStatementListResponse(BaseModel):
    """
    object model
    """

    result: Optional[V3financeCashFlowStatementListResponseResult] = Field(alias="result", default=None)
