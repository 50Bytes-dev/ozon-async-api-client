from typing import *

from pydantic import BaseModel, Field


class GetSellerActionsV1responseAction(BaseModel):
    """
    object model
    """

    id: Optional[float] = Field(alias="id", default=None)

    title: Optional[str] = Field(alias="title", default=None)

    action_type: Optional[str] = Field(alias="action_type", default=None)

    description: Optional[str] = Field(alias="description", default=None)

    date_start: Optional[str] = Field(alias="date_start", default=None)

    date_end: Optional[str] = Field(alias="date_end", default=None)

    freeze_date: Optional[Union[str, int]] = Field(alias="freeze_date", default=None)

    potential_products_count: Optional[float] = Field(alias="potential_products_count", default=None)

    participating_products_count: Optional[float] = Field(alias="participating_products_count", default=None)

    is_participating: Optional[bool] = Field(alias="is_participating", default=None)

    is_voucher_action: Optional[bool] = Field(alias="is_voucher_action", default=None)

    banned_products_count: Optional[float] = Field(alias="banned_products_count", default=None)

    with_targeting: Optional[bool] = Field(alias="with_targeting", default=None)

    order_amount: Optional[float] = Field(alias="order_amount", default=None)

    discount_type: Optional[str] = Field(alias="discount_type", default=None)

    discount_value: Optional[float] = Field(alias="discount_value", default=None)
