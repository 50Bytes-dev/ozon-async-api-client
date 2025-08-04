from typing import *

from pydantic import BaseModel, Field


class ArrivalpassArrivalPassUpdateRequestArrivalPass(BaseModel):
    """
    object model
    """

    arrival_pass_id: int = Field(alias="arrival_pass_id")

    arrival_time: str = Field(alias="arrival_time")

    driver_name: str = Field(alias="driver_name")

    driver_phone: str = Field(alias="driver_phone")

    vehicle_license_plate: str = Field(alias="vehicle_license_plate")

    vehicle_model: str = Field(alias="vehicle_model")
