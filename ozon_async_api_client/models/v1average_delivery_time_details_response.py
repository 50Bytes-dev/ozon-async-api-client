from typing import *

from pydantic import BaseModel, Field

from .v1average_delivery_time_details_response_data import V1averageDeliveryTimeDetailsResponseData


class V1averageDeliveryTimeDetailsResponse(BaseModel):
    """
    None model
    """

    data: Optional[List[Optional[V1averageDeliveryTimeDetailsResponseData]]] = Field(alias="data", default=None)

    total_rows: Optional[int] = Field(alias="total_rows", default=None)
