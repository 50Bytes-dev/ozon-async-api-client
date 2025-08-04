from typing import *

from pydantic import BaseModel, Field


class AnalyticsStockOnWarehouseResultRows(BaseModel):
    """
    object model
    """

    sku: Optional[int] = Field(alias="sku", default=None)

    item_code: Optional[Union[str, int]] = Field(alias="item_code", default=None)

    item_name: Optional[str] = Field(alias="item_name", default=None)

    free_to_sell_amount: Optional[int] = Field(alias="free_to_sell_amount", default=None)

    promised_amount: Optional[int] = Field(alias="promised_amount", default=None)

    reserved_amount: Optional[int] = Field(alias="reserved_amount", default=None)

    warehouse_name: Optional[str] = Field(alias="warehouse_name", default=None)
