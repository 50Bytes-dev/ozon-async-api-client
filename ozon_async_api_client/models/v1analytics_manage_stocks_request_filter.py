from typing import *

from pydantic import BaseModel, Field


class V1analyticsManageStocksRequestFilter(BaseModel):
    """
    object model

    Фильтр.
    """

    skus: Optional[List[int]] = Field(alias="skus", default=None)

    stock_types: Optional[List[str]] = Field(alias="stock_types", default=None)

    warehouse_ids: Optional[List[int]] = Field(alias="warehouse_ids", default=None)
