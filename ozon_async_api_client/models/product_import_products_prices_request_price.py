from typing import *

from pydantic import BaseModel, Field


class ProductImportProductsPricesRequestPrice(BaseModel):
    """
    object model
    """

    auto_action_enabled: Optional[str] = Field(alias="auto_action_enabled", default=None)

    auto_add_to_ozon_actions_list_enabled: Optional[str] = Field(
        alias="auto_add_to_ozon_actions_list_enabled", default=None
    )

    currency_code: Optional[str] = Field(alias="currency_code", default=None)

    min_price: Optional[str] = Field(alias="min_price", default=None)

    min_price_for_auto_actions_enabled: Optional[bool] = Field(alias="min_price_for_auto_actions_enabled", default=None)

    net_price: Optional[str] = Field(alias="net_price", default=None)

    offer_id: Optional[Union[str, int]] = Field(alias="offer_id", default=None)

    old_price: Optional[str] = Field(alias="old_price", default=None)

    price: Optional[str] = Field(alias="price", default=None)

    price_strategy_enabled: Optional[str] = Field(alias="price_strategy_enabled", default=None)

    product_id: Optional[int] = Field(alias="product_id", default=None)

    quant_size: Optional[int] = Field(alias="quant_size", default=None)

    vat: Optional[str] = Field(alias="vat", default=None)
