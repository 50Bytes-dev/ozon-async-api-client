from typing import *

from pydantic import BaseModel, Field


class SupplyCheckExpireDatePresentedRule(BaseModel):
    """
    None model

    Правило указания сроков годности для товаров.
    """

    count_sku_with_expiration: Optional[int] = Field(alias="count_sku_with_expiration", default=None)

    count_sku_with_expiration_filled: Optional[int] = Field(alias="count_sku_with_expiration_filled", default=None)

    is_applicable: Optional[bool] = Field(alias="is_applicable", default=None)

    is_required: Optional[bool] = Field(alias="is_required", default=None)

    satisfied: Optional[bool] = Field(alias="satisfied", default=None)
