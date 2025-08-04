from typing import *

from pydantic import BaseModel, Field


class GetSupplyOrderBundleRequestItemTagsCalculation(BaseModel):
    """
    object model

    Список складов для расчёта товарных тегов.
    """

    dropoff_warehouse_id: str = Field(alias="dropoff_warehouse_id")

    storage_warehouse_ids: List[str] = Field(alias="storage_warehouse_ids")
