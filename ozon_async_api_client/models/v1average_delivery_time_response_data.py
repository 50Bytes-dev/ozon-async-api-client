from typing import *

from pydantic import BaseModel, Field

from .v1average_delivery_time_response_clusters_data import V1averageDeliveryTimeResponseClustersData
from .v1average_delivery_time_response_metrics import V1averageDeliveryTimeResponseMetrics


class V1averageDeliveryTimeResponseData(BaseModel):
    """
    None model
    """

    clusters_data: Optional[List[Optional[V1averageDeliveryTimeResponseClustersData]]] = Field(
        alias="clusters_data", default=None
    )

    delivery_cluster_id: Optional[int] = Field(alias="delivery_cluster_id", default=None)

    metrics: Optional[V1averageDeliveryTimeResponseMetrics] = Field(alias="metrics", default=None)
