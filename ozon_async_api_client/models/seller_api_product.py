from typing import *

from pydantic import BaseModel, Field


class SellerApiProduct(BaseModel):
    """
    object model
    """

    id: Optional[float] = Field(alias="id", default=None)

    price: Optional[float] = Field(alias="price", default=None)

    action_price: Optional[float] = Field(alias="action_price", default=None)

    alert_max_action_price_failed: Optional[bool] = Field(alias="alert_max_action_price_failed", default=None)

    alert_max_action_price: Optional[float] = Field(alias="alert_max_action_price", default=None)

    max_action_price: Optional[float] = Field(alias="max_action_price", default=None)

    add_mode: Optional[str] = Field(alias="add_mode", default=None)

    min_stock: Optional[float] = Field(alias="min_stock", default=None)

    stock: Optional[float] = Field(alias="stock", default=None)
