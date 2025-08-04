from typing import *

from pydantic import BaseModel, Field


class V1vehicleInfo(BaseModel):
    """
    object model

    Информация о водителе и автомобиле.
    """

    driver_name: str = Field(alias="driver_name")

    driver_phone: str = Field(alias="driver_phone")

    vehicle_model: str = Field(alias="vehicle_model")

    vehicle_number: str = Field(alias="vehicle_number")
