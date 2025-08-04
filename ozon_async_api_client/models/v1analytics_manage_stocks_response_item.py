from typing import *

from pydantic import BaseModel, Field


class V1analyticsManageStocksResponseItem(BaseModel):
    """
    object model
    """

    defect_stock_count: Optional[int] = Field(alias="defect_stock_count", default=None)

    expiring_stock_count: Optional[int] = Field(alias="expiring_stock_count", default=None)

    name: Optional[str] = Field(alias="name", default=None)

    offer_id: Optional[Union[str, int]] = Field(alias="offer_id", default=None)

    sku: Optional[int] = Field(alias="sku", default=None)

    valid_stock_count: Optional[int] = Field(alias="valid_stock_count", default=None)

    waitingdocs_stock_count: Optional[int] = Field(alias="waitingdocs_stock_count", default=None)

    warehouse_name: Optional[str] = Field(alias="warehouse_name", default=None)
