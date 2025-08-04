from typing import *

from pydantic import BaseModel, Field

from .analytics_stock_on_warehouse_response_result import AnalyticsStockOnWarehouseResponseResult


class AnalyticsStockOnWarehouseResponse(BaseModel):
    """
    object model
    """

    result: Optional[AnalyticsStockOnWarehouseResponseResult] = Field(alias="result", default=None)
