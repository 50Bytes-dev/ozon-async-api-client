from typing import *

from pydantic import BaseModel, Field

from .v1average_delivery_time_response_clusters_data_amnesty import V1averageDeliveryTimeResponseClustersDataAmnesty
from .v1average_delivery_time_response_delivery_time_status import V1averageDeliveryTimeResponseDeliveryTimeStatus


class V1averageDeliveryTimeResponseClustersData(BaseModel):
    """
    None model
    """

    another_delivery_time: Optional[List[Optional[V1averageDeliveryTimeResponseClustersDataAmnesty]]] = Field(
        alias="another_delivery_time", default=None
    )

    cluster_id: Optional[int] = Field(alias="cluster_id", default=None)

    delivery_time_FBO: Optional[int] = Field(alias="delivery_time_FBO", default=None)

    delivery_time_FBS: Optional[float] = Field(alias="delivery_time_FBS", default=None)

    delivery_time_status: Optional[V1averageDeliveryTimeResponseDeliveryTimeStatus] = Field(
        alias="delivery_time_status", default=None
    )

    orders_count: Optional[int] = Field(alias="orders_count", default=None)

    orders_percent: Optional[int] = Field(alias="orders_percent", default=None)
