from typing import *

from pydantic import BaseModel, Field


class V2vehicleInfo(BaseModel):
    """
    object model
    """

    driver_name: Optional[str] = Field(alias="driver_name", default=None)

    driver_phone: Optional[str] = Field(alias="driver_phone", default=None)

    vehicle_model: Optional[str] = Field(alias="vehicle_model", default=None)

    vehicle_number: Optional[str] = Field(alias="vehicle_number", default=None)
