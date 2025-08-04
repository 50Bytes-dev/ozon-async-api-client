from typing import *

from pydantic import BaseModel, Field

from .details_delivery_details import DetailsDeliveryDetails
from .details_others import DetailsOthers
from .details_return_details import DetailsReturnDetails
from .details_rfbs_details import DetailsRfbsDetails
from .details_service import DetailsService
from .v3finance_cash_flow_statement_list_response_period import V3financeCashFlowStatementListResponsePeriod


class FinanceCashFlowStatementListResponseDetails(BaseModel):
    """
    object model

    Детализированная информация.
    """

    begin_balance_amount: Optional[float] = Field(alias="begin_balance_amount", default=None)

    delivery: Optional[DetailsDeliveryDetails] = Field(alias="delivery", default=None)

    invoice_transfer: Optional[float] = Field(alias="invoice_transfer", default=None)

    loan: Optional[float] = Field(alias="loan", default=None)

    payments: Optional[List[Any]] = Field(alias="payments", default=None)

    period: Optional[V3financeCashFlowStatementListResponsePeriod] = Field(alias="period", default=None)

    return_: Optional[DetailsReturnDetails] = Field(alias="return", default=None)

    rfbs: Optional[DetailsRfbsDetails] = Field(alias="rfbs", default=None)

    services: Optional[DetailsService] = Field(alias="services", default=None)

    others: Optional[DetailsOthers] = Field(alias="others", default=None)

    end_balance_amount: Optional[float] = Field(alias="end_balance_amount", default=None)
