from typing import *

from pydantic import BaseModel, Field

from .v2supply_state import V2supplyState


class V2orderSupply(BaseModel):
    """
    object model
    """

    bundle_id: Optional[str] = Field(alias="bundle_id", default=None)

    storage_warehouse_id: Optional[int] = Field(alias="storage_warehouse_id", default=None)

    supply_id: Optional[int] = Field(alias="supply_id", default=None)

    supply_state: Optional[V2supplyState] = Field(alias="supply_state", default=None)

    supply_tags: Optional[Any] = Field(alias="supply_tags", default=None)
