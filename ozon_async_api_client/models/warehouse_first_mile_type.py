from typing import *

from pydantic import BaseModel, Field


class WarehouseFirstMileType(BaseModel):
    """
    object model

    Первая миля FBS.
    """

    dropoff_point_id: Optional[Union[str, int]] = Field(alias="dropoff_point_id", default=None)

    dropoff_timeslot_id: Optional[int] = Field(alias="dropoff_timeslot_id", default=None)

    first_mile_is_changing: Optional[bool] = Field(alias="first_mile_is_changing", default=None)

    first_mile_type: Optional[str] = Field(alias="first_mile_type", default=None)
