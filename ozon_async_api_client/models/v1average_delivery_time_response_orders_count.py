from typing import *

from pydantic import BaseModel, Field

from .v1average_delivery_time_response_orders_count_value_fast import V1averageDeliveryTimeResponseOrdersCountValueFast
from .v1average_delivery_time_response_orders_count_value_long import V1averageDeliveryTimeResponseOrdersCountValueLong
from .v1average_delivery_time_response_orders_count_value_medium import \
    V1averageDeliveryTimeResponseOrdersCountValueMedium


class V1averageDeliveryTimeResponseOrdersCount(BaseModel):
    """
    None model

    Количество заказанных товаров из кластера отгрузки.
    """

    fast: Optional[V1averageDeliveryTimeResponseOrdersCountValueFast] = Field(alias="fast", default=None)

    long: Optional[V1averageDeliveryTimeResponseOrdersCountValueLong] = Field(alias="long", default=None)

    medium: Optional[V1averageDeliveryTimeResponseOrdersCountValueMedium] = Field(alias="medium", default=None)

    total: Optional[int] = Field(alias="total", default=None)
