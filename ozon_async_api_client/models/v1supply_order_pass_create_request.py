from typing import *

from pydantic import BaseModel, Field

from .v1vehicle_info import V1vehicleInfo


class V1supplyOrderPassCreateRequest(BaseModel):
    """
    None model
    """

    supply_order_id: int = Field(alias="supply_order_id")

    vehicle: V1vehicleInfo = Field(alias="vehicle")
