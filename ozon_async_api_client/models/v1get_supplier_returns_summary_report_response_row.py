from typing import *

from pydantic import BaseModel, Field


class V1getSupplierReturnsSummaryReportResponseRow(BaseModel):
    """
    None model
    """

    barcode: Optional[str] = Field(alias="barcode", default=None)

    box_barcode: Optional[str] = Field(alias="box_barcode", default=None)

    box_height: Optional[float] = Field(alias="box_height", default=None)

    box_id: Optional[int] = Field(alias="box_id", default=None)

    box_length: Optional[float] = Field(alias="box_length", default=None)

    box_state: Optional[str] = Field(alias="box_state", default=None)

    box_volume: Optional[float] = Field(alias="box_volume", default=None)

    box_weight: Optional[float] = Field(alias="box_weight", default=None)

    box_width: Optional[float] = Field(alias="box_width", default=None)

    clearing_warehouse_name: Optional[str] = Field(alias="clearing_warehouse_name", default=None)

    delivery_date: Optional[str] = Field(alias="delivery_date", default=None)

    delivery_type: Optional[str] = Field(alias="delivery_type", default=None)

    destination_warehouse_address: Optional[str] = Field(alias="destination_warehouse_address", default=None)

    destination_warehouse_name: Optional[str] = Field(alias="destination_warehouse_name", default=None)

    given_out_date: Optional[str] = Field(alias="given_out_date", default=None)

    is_auto_return: Optional[bool] = Field(alias="is_auto_return", default=None)

    name: Optional[str] = Field(alias="name", default=None)

    offer_id: Optional[str] = Field(alias="offer_id", default=None)

    preliminary_delivery_price: Optional[float] = Field(alias="preliminary_delivery_price", default=None)

    quant_count: Optional[int] = Field(alias="quant_count", default=None)

    quantity_for_return: Optional[int] = Field(alias="quantity_for_return", default=None)

    return_created_at: Optional[str] = Field(alias="return_created_at", default=None)

    return_id: Optional[int] = Field(alias="return_id", default=None)

    return_state: Optional[str] = Field(alias="return_state", default=None)

    sku: Optional[int] = Field(alias="sku", default=None)

    stock_type: Optional[str] = Field(alias="stock_type", default=None)

    utilization_date: Optional[str] = Field(alias="utilization_date", default=None)
