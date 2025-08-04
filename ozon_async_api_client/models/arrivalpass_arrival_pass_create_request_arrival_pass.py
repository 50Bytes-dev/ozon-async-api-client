from typing import *

from pydantic import BaseModel, Field


class ArrivalpassArrivalPassCreateRequestArrivalPass(BaseModel):
    """
    object model
    """

    arrival_time: str = Field(alias="arrival_time")

    driver_name: str = Field(alias="driver_name")

    driver_phone: str = Field(alias="driver_phone")

    dropoff_point_id: int = Field(alias="dropoff_point_id")

    vehicle_license_plate: str = Field(alias="vehicle_license_plate")

    vehicle_model: str = Field(alias="vehicle_model")

    warehouse_id: int = Field(alias="warehouse_id")
