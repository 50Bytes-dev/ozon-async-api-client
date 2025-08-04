from typing import *

from pydantic import BaseModel, Field

from .average_delivery_time_response_total import AverageDeliveryTimeResponseTotal
from .v1average_delivery_time_response_data import V1averageDeliveryTimeResponseData


class V1averageDeliveryTimeResponse(BaseModel):
    """
    None model
    """

    data: Optional[List[Optional[V1averageDeliveryTimeResponseData]]] = Field(alias="data", default=None)

    total: Optional[AverageDeliveryTimeResponseTotal] = Field(alias="total", default=None)
