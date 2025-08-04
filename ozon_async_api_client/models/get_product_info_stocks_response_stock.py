from typing import *

from pydantic import BaseModel, Field

from .stock_shipment_type import StockShipmentType


class GetProductInfoStocksResponseStock(BaseModel):
    """
    None model
    """

    present: Optional[int] = Field(alias="present", default=None)

    reserved: Optional[int] = Field(alias="reserved", default=None)

    shipment_type: Optional[StockShipmentType] = Field(alias="shipment_type", default=None)

    sku: Optional[int] = Field(alias="sku", default=None)

    type: Optional[str] = Field(alias="type", default=None)

    warehouse_ids: Optional[List[int]] = Field(alias="warehouse_ids", default=None)
