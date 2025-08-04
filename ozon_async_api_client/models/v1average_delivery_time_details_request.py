from typing import *

from pydantic import BaseModel, Field

from .average_delivery_time_details_request_filters import AverageDeliveryTimeDetailsRequestFilters


class V1averageDeliveryTimeDetailsRequest(BaseModel):
    """
    None model
    """

    cluster_id: int = Field(alias="cluster_id")

    filters: Optional[AverageDeliveryTimeDetailsRequestFilters] = Field(alias="filters", default=None)

    limit: int = Field(alias="limit")

    offset: int = Field(alias="offset")
