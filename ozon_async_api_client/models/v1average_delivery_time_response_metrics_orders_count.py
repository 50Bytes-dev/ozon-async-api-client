from typing import *

from pydantic import BaseModel, Field

from .v1average_delivery_time_response_metrics_orders_count_value_fast import \
    V1averageDeliveryTimeResponseMetricsOrdersCountValueFast
from .v1average_delivery_time_response_metrics_orders_count_value_long import \
    V1averageDeliveryTimeResponseMetricsOrdersCountValueLong
from .v1average_delivery_time_response_metrics_orders_count_value_medium import \
    V1averageDeliveryTimeResponseMetricsOrdersCountValueMedium


class V1averageDeliveryTimeResponseMetricsOrdersCount(BaseModel):
    """
    None model

    Количество заказанных товаров.
    """

    fast: Optional[V1averageDeliveryTimeResponseMetricsOrdersCountValueFast] = Field(alias="fast", default=None)

    long: Optional[V1averageDeliveryTimeResponseMetricsOrdersCountValueLong] = Field(alias="long", default=None)

    medium: Optional[V1averageDeliveryTimeResponseMetricsOrdersCountValueMedium] = Field(alias="medium", default=None)

    total: Optional[int] = Field(alias="total", default=None)
