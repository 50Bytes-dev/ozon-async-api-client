from typing import *

from pydantic import BaseModel, Field

from .finance_cash_flow_statement_list_response_service import FinanceCashFlowStatementListResponseService


class DetailsService(BaseModel):
    """
    object model

    Услуги.
    """

    total: Optional[float] = Field(alias="total", default=None)

    items: Optional[List[Optional[FinanceCashFlowStatementListResponseService]]] = Field(alias="items", default=None)
