from typing import *

from pydantic import BaseModel, Field

from .delivery_method_list_response_delivery_method import DeliveryMethodListResponseDeliveryMethod


class WarehouseDeliveryMethodListResponse(BaseModel):
    """
    object model
    """

    has_next: Optional[bool] = Field(alias="has_next", default=None)

    result: Optional[List[Optional[DeliveryMethodListResponseDeliveryMethod]]] = Field(alias="result", default=None)
