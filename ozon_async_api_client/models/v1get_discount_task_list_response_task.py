from typing import *

from pydantic import BaseModel, Field


class V1getDiscountTaskListResponseTask(BaseModel):
    """
    object model
    """

    id: Optional[int] = Field(alias="id", default=None)

    created_at: Optional[str] = Field(alias="created_at", default=None)

    end_at: Optional[str] = Field(alias="end_at", default=None)

    edited_till: Optional[str] = Field(alias="edited_till", default=None)

    status: Optional[str] = Field(alias="status", default=None)

    customer_name: Optional[str] = Field(alias="customer_name", default=None)

    sku: Optional[int] = Field(alias="sku", default=None)

    user_comment: Optional[str] = Field(alias="user_comment", default=None)

    seller_comment: Optional[str] = Field(alias="seller_comment", default=None)

    requested_price: Optional[float] = Field(alias="requested_price", default=None)

    approved_price: Optional[float] = Field(alias="approved_price", default=None)

    original_price: Optional[float] = Field(alias="original_price", default=None)

    discount: Optional[float] = Field(alias="discount", default=None)

    discount_percent: Optional[float] = Field(alias="discount_percent", default=None)

    base_price: Optional[float] = Field(alias="base_price", default=None)

    min_auto_price: Optional[float] = Field(alias="min_auto_price", default=None)

    prev_task_id: Optional[int] = Field(alias="prev_task_id", default=None)

    is_damaged: Optional[bool] = Field(alias="is_damaged", default=None)

    moderated_at: Optional[str] = Field(alias="moderated_at", default=None)

    approved_discount: Optional[float] = Field(alias="approved_discount", default=None)

    approved_discount_percent: Optional[float] = Field(alias="approved_discount_percent", default=None)

    is_purchased: Optional[bool] = Field(alias="is_purchased", default=None)

    is_auto_moderated: Optional[bool] = Field(alias="is_auto_moderated", default=None)

    offer_id: Optional[Union[str, int]] = Field(alias="offer_id", default=None)

    email: Optional[str] = Field(alias="email", default=None)

    last_name: Optional[str] = Field(alias="last_name", default=None)

    first_name: Optional[str] = Field(alias="first_name", default=None)

    patronymic: Optional[str] = Field(alias="patronymic", default=None)

    approved_quantity_min: Optional[int] = Field(alias="approved_quantity_min", default=None)

    approved_quantity_max: Optional[int] = Field(alias="approved_quantity_max", default=None)

    requested_quantity_min: Optional[int] = Field(alias="requested_quantity_min", default=None)

    requested_quantity_max: Optional[int] = Field(alias="requested_quantity_max", default=None)

    requested_price_with_fee: Optional[float] = Field(alias="requested_price_with_fee", default=None)

    approved_price_with_fee: Optional[float] = Field(alias="approved_price_with_fee", default=None)

    approved_price_fee_percent: Optional[float] = Field(alias="approved_price_fee_percent", default=None)
