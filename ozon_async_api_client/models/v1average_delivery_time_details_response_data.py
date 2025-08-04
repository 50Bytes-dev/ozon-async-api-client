from typing import *

from pydantic import BaseModel, Field

from .average_delivery_time_details_response_item_data import AverageDeliveryTimeDetailsResponseItemData
from .v1average_delivery_time_details_response_clusters_data import V1averageDeliveryTimeDetailsResponseClustersData
from .v1average_delivery_time_details_response_metrics import V1averageDeliveryTimeDetailsResponseMetrics


class V1averageDeliveryTimeDetailsResponseData(BaseModel):
    """
    None model
    """

    clusters_data: Optional[List[Optional[V1averageDeliveryTimeDetailsResponseClustersData]]] = Field(
        alias="clusters_data", default=None
    )

    item: Optional[AverageDeliveryTimeDetailsResponseItemData] = Field(alias="item", default=None)

    metrics: Optional[V1averageDeliveryTimeDetailsResponseMetrics] = Field(alias="metrics", default=None)
