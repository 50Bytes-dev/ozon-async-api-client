from typing import *

from pydantic import BaseModel, Field

from .v1average_delivery_time_details_response_metrics_orders_count_value_fast import \
    V1averageDeliveryTimeDetailsResponseMetricsOrdersCountValueFast
from .v1average_delivery_time_details_response_metrics_orders_count_value_long import \
    V1averageDeliveryTimeDetailsResponseMetricsOrdersCountValueLong
from .v1average_delivery_time_details_response_metrics_orders_count_value_medium import \
    V1averageDeliveryTimeDetailsResponseMetricsOrdersCountValueMedium


class V1averageDeliveryTimeDetailsResponseMetricsOrdersCount(BaseModel):
    """
    None model

    Заказано товаров по нормативному времени доставки.
    """

    fast: Optional[V1averageDeliveryTimeDetailsResponseMetricsOrdersCountValueFast] = Field(alias="fast", default=None)

    long: Optional[V1averageDeliveryTimeDetailsResponseMetricsOrdersCountValueLong] = Field(alias="long", default=None)

    medium: Optional[V1averageDeliveryTimeDetailsResponseMetricsOrdersCountValueMedium] = Field(
        alias="medium", default=None
    )

    total: Optional[int] = Field(alias="total", default=None)
