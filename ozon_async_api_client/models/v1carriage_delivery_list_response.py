from typing import *

from pydantic import BaseModel, Field

from .v1carriage_delivery_list_response_result import V1carriageDeliveryListResponseResult


class V1carriageDeliveryListResponse(BaseModel):
    """
    None model
    """

    result: Optional[List[Optional[V1carriageDeliveryListResponseResult]]] = Field(alias="result", default=None)
