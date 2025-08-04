from typing import *

from pydantic import BaseModel, Field


class PostingFinancialDataProduct(BaseModel):
    """
    object model
    """

    actions: Optional[List[str]] = Field(alias="actions", default=None)

    currency_code: Optional[str] = Field(alias="currency_code", default=None)

    commission_amount: Optional[float] = Field(alias="commission_amount", default=None)

    commission_percent: Optional[int] = Field(alias="commission_percent", default=None)

    commissions_currency_code: Optional[str] = Field(alias="commissions_currency_code", default=None)

    old_price: Optional[float] = Field(alias="old_price", default=None)

    payout: Optional[float] = Field(alias="payout", default=None)

    price: Optional[float] = Field(alias="price", default=None)

    product_id: Optional[int] = Field(alias="product_id", default=None)

    quantity: Optional[int] = Field(alias="quantity", default=None)

    total_discount_percent: Optional[float] = Field(alias="total_discount_percent", default=None)

    total_discount_value: Optional[float] = Field(alias="total_discount_value", default=None)
