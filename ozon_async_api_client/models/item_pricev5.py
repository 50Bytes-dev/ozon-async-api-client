from typing import *

from pydantic import BaseModel, Field


class ItemPricev5(BaseModel):
    """
    object model

    Цена товара.
    """

    auto_action_enabled: Optional[bool] = Field(alias="auto_action_enabled", default=None)

    auto_add_to_ozon_actions_list_enabled: Optional[bool] = Field(
        alias="auto_add_to_ozon_actions_list_enabled", default=None
    )

    currency_code: Optional[str] = Field(alias="currency_code", default=None)

    marketing_price: Optional[float] = Field(alias="marketing_price", default=None)

    marketing_seller_price: Optional[float] = Field(alias="marketing_seller_price", default=None)

    min_price: Optional[float] = Field(alias="min_price", default=None)

    net_price: Optional[float] = Field(alias="net_price", default=None)

    old_price: Optional[float] = Field(alias="old_price", default=None)

    price: Optional[float] = Field(alias="price", default=None)

    retail_price: Optional[float] = Field(alias="retail_price", default=None)

    vat: Optional[float] = Field(alias="vat", default=None)
