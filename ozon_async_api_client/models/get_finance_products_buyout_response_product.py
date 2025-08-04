from typing import *

from pydantic import BaseModel, Field


class GetFinanceProductsBuyoutResponseProduct(BaseModel):
    """
    None model
    """

    amount: Optional[float] = Field(alias="amount", default=None)

    buyout_price: Optional[float] = Field(alias="buyout_price", default=None)

    deduction_by_category_percent: Optional[float] = Field(alias="deduction_by_category_percent", default=None)

    name: Optional[str] = Field(alias="name", default=None)

    offer_id: Optional[Union[str, int]] = Field(alias="offer_id", default=None)

    posting_number: Optional[str] = Field(alias="posting_number", default=None)

    quantity: Optional[int] = Field(alias="quantity", default=None)

    seller_price_per_instance: Optional[float] = Field(alias="seller_price_per_instance", default=None)

    sku: Optional[int] = Field(alias="sku", default=None)

    vat_percent: Optional[int] = Field(alias="vat_percent", default=None)
