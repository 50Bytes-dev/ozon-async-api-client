from typing import *

from pydantic import BaseModel, Field

from .delivery_method_list_request_filter import DeliveryMethodListRequestFilter


class WarehouseDeliveryMethodListRequest(BaseModel):
    """
    object model
    """

    filter: Optional[DeliveryMethodListRequestFilter] = Field(alias="filter", default=None)

    limit: int = Field(alias="limit")

    offset: Optional[int] = Field(alias="offset", default=None)
