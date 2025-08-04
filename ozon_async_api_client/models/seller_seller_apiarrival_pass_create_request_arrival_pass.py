from typing import *

from pydantic import BaseModel, Field


class SellerSellerAPIArrivalPassCreateRequestArrivalPass(BaseModel):
    """
    object model
    """

    driver_name: str = Field(alias="driver_name")

    driver_phone: str = Field(alias="driver_phone")

    vehicle_license_plate: str = Field(alias="vehicle_license_plate")

    vehicle_model: str = Field(alias="vehicle_model")

    with_returns: Optional[bool] = Field(alias="with_returns", default=None)
