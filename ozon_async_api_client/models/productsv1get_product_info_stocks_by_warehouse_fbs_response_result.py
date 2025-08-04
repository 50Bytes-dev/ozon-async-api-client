from typing import *

from pydantic import BaseModel, Field


class Productsv1getProductInfoStocksByWarehouseFbsResponseResult(BaseModel):
    """
    object model
    """

    sku: Optional[int] = Field(alias="sku", default=None)

    present: Optional[int] = Field(alias="present", default=None)

    product_id: Optional[int] = Field(alias="product_id", default=None)

    reserved: Optional[int] = Field(alias="reserved", default=None)

    warehouse_id: Optional[int] = Field(alias="warehouse_id", default=None)

    warehouse_name: Optional[str] = Field(alias="warehouse_name", default=None)
