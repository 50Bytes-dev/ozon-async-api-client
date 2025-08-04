from typing import *

from pydantic import BaseModel, Field


class ArrivalPassListRequestFilter(BaseModel):
    """
    object model

    Фильтры.
    """

    arrival_pass_ids: Optional[List[int]] = Field(alias="arrival_pass_ids", default=None)

    arrival_reason: Optional[str] = Field(alias="arrival_reason", default=None)

    dropoff_point_ids: Optional[List[int]] = Field(alias="dropoff_point_ids", default=None)

    only_active_passes: Optional[bool] = Field(alias="only_active_passes", default=None)

    warehouse_ids: Optional[List[int]] = Field(alias="warehouse_ids", default=None)
