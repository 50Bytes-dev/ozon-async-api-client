from typing import *

from pydantic import BaseModel, Field


class Financev3financeTransactionTotalsV3responseResult(BaseModel):
    """
    object model

    Результаты запроса.
    """

    accruals_for_sale: Optional[float] = Field(alias="accruals_for_sale", default=None)

    compensation_amount: Optional[float] = Field(alias="compensation_amount", default=None)

    money_transfer: Optional[float] = Field(alias="money_transfer", default=None)

    others_amount: Optional[float] = Field(alias="others_amount", default=None)

    processing_and_delivery: Optional[float] = Field(alias="processing_and_delivery", default=None)

    refunds_and_cancellations: Optional[float] = Field(alias="refunds_and_cancellations", default=None)

    sale_commission: Optional[float] = Field(alias="sale_commission", default=None)

    services_amount: Optional[float] = Field(alias="services_amount", default=None)
