from typing import *

from pydantic import BaseModel, Field


class ArrivalpassArrivalPassListResponseArrivalPass(BaseModel):
    """
    object model
    """

    arrival_pass_id: Optional[int] = Field(alias="arrival_pass_id", default=None)

    arrival_reasons: Optional[List[str]] = Field(alias="arrival_reasons", default=None)

    arrival_time: Optional[str] = Field(alias="arrival_time", default=None)

    driver_name: Optional[str] = Field(alias="driver_name", default=None)

    driver_phone: Optional[str] = Field(alias="driver_phone", default=None)

    dropoff_point_id: Optional[int] = Field(alias="dropoff_point_id", default=None)

    is_active: Optional[bool] = Field(alias="is_active", default=None)

    vehicle_license_plate: Optional[str] = Field(alias="vehicle_license_plate", default=None)

    vehicle_model: Optional[str] = Field(alias="vehicle_model", default=None)

    warehouse_id: Optional[int] = Field(alias="warehouse_id", default=None)
