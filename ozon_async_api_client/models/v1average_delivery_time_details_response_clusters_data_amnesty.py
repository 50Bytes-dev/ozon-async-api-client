from typing import *

from pydantic import BaseModel, Field

from .v1average_delivery_time_details_response_delivery_time_status import \
    V1averageDeliveryTimeDetailsResponseDeliveryTimeStatus


class V1averageDeliveryTimeDetailsResponseClustersDataAmnesty(BaseModel):
    """
    None model
    """

    delivery_time: Optional[int] = Field(alias="delivery_time", default=None)

    delivery_time_status: Optional[V1averageDeliveryTimeDetailsResponseDeliveryTimeStatus] = Field(
        alias="delivery_time_status", default=None
    )

    orders_count: Optional[int] = Field(alias="orders_count", default=None)

    orders_percent: Optional[int] = Field(alias="orders_percent", default=None)
