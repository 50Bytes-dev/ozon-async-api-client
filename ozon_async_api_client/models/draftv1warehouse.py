from typing import *

from pydantic import BaseModel, Field

from .v1bundle_id import V1bundleId
from .v1supply_warehouse import V1supplyWarehouse
from .v1warehouse_status import V1warehouseStatus


class Draftv1warehouse(BaseModel):
    """
    None model
    """

    bundle_ids: Optional[List[Optional[V1bundleId]]] = Field(alias="bundle_ids", default=None)

    restricted_bundle_id: Optional[str] = Field(alias="restricted_bundle_id", default=None)

    status: Optional[V1warehouseStatus] = Field(alias="status", default=None)

    supply_warehouse: Optional[V1supplyWarehouse] = Field(alias="supply_warehouse", default=None)

    total_rank: Optional[int] = Field(alias="total_rank", default=None)

    total_score: Optional[float] = Field(alias="total_score", default=None)

    travel_time_days: Optional[int] = Field(alias="travel_time_days", default=None)
