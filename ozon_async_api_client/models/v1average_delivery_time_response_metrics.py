from typing import *

from pydantic import BaseModel, Field

from .attention_level_enum import AttentionLevelEnum
from .v1average_delivery_time_response_delivery_time_status import V1averageDeliveryTimeResponseDeliveryTimeStatus
from .v1average_delivery_time_response_metrics_orders_count import V1averageDeliveryTimeResponseMetricsOrdersCount


class V1averageDeliveryTimeResponseMetrics(BaseModel):
    """
    None model

    Метрики доставки.
    """

    attention_level: Optional[AttentionLevelEnum] = Field(alias="attention_level", default=None)

    average_delivery_time: Optional[int] = Field(alias="average_delivery_time", default=None)

    average_delivery_time_status: Optional[V1averageDeliveryTimeResponseDeliveryTimeStatus] = Field(
        alias="average_delivery_time_status", default=None
    )

    impact_share: Optional[int] = Field(alias="impact_share", default=None)

    exact_impact_share: Optional[str] = Field(alias="exact_impact_share", default=None)

    lost_profit: Optional[int] = Field(alias="lost_profit", default=None)

    orders_count: Optional[V1averageDeliveryTimeResponseMetricsOrdersCount] = Field(alias="orders_count", default=None)

    recommended_supply: Optional[int] = Field(alias="recommended_supply", default=None)
