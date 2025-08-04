from typing import *

from pydantic import BaseModel, Field

from .v1day import V1day


class V1dropOffWarehouse(BaseModel):
    """
    None model
    """

    current_time_in_timezone: Optional[str] = Field(alias="current_time_in_timezone", default=None)

    days: Optional[List[Optional[V1day]]] = Field(alias="days", default=None)

    drop_off_warehouse_id: Optional[int] = Field(alias="drop_off_warehouse_id", default=None)

    warehouse_timezone: Optional[str] = Field(alias="warehouse_timezone", default=None)
