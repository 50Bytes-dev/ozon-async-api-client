from typing import *

from pydantic import BaseModel, Field

from .analytics_get_stock_on_warehouses_request_warehouse_type import AnalyticsGetStockOnWarehousesRequestWarehouseType


class AnalyticsStockOnWarehouseRequest(BaseModel):
    """
    object model
    """

    limit: int = Field(alias="limit")

    offset: Optional[int] = Field(alias="offset", default=None)

    warehouse_type: Optional[AnalyticsGetStockOnWarehousesRequestWarehouseType] = Field(
        alias="warehouse_type", default=None
    )
