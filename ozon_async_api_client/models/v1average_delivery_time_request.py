from typing import *

from pydantic import BaseModel, Field

from .v1average_delivery_time_request_delivery_schema import V1averageDeliveryTimeRequestDeliverySchema
from .v1average_delivery_time_request_supply_period import V1averageDeliveryTimeRequestSupplyPeriod


class V1averageDeliveryTimeRequest(BaseModel):
    """
    None model
    """

    delivery_schema: V1averageDeliveryTimeRequestDeliverySchema = Field(alias="delivery_schema")

    sku: Optional[List[int]] = Field(alias="sku", default=None)

    supply_period: V1averageDeliveryTimeRequestSupplyPeriod = Field(alias="supply_period")
