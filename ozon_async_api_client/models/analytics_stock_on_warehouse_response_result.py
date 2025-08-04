from typing import *

from pydantic import BaseModel, Field

from .analytics_stock_on_warehouse_result_rows import AnalyticsStockOnWarehouseResultRows


class AnalyticsStockOnWarehouseResponseResult(BaseModel):
    """
    object model

    Результат запроса.
    """

    rows: Optional[List[Optional[AnalyticsStockOnWarehouseResultRows]]] = Field(alias="rows", default=None)
