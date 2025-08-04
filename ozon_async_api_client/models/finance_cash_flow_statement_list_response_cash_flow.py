from typing import *

from pydantic import BaseModel, Field

from .v3finance_cash_flow_statement_list_response_period import V3financeCashFlowStatementListResponsePeriod


class FinanceCashFlowStatementListResponseCashFlow(BaseModel):
    """
    object model
    """

    period: Optional[V3financeCashFlowStatementListResponsePeriod] = Field(alias="period", default=None)

    orders_amount: Optional[float] = Field(alias="orders_amount", default=None)

    returns_amount: Optional[float] = Field(alias="returns_amount", default=None)

    commission_amount: Optional[float] = Field(alias="commission_amount", default=None)

    services_amount: Optional[float] = Field(alias="services_amount", default=None)

    item_delivery_and_return_amount: Optional[float] = Field(alias="item_delivery_and_return_amount", default=None)

    currency_code: Optional[str] = Field(alias="currency_code", default=None)
