from typing import *

from pydantic import BaseModel, Field

from .v1get_product_info_subscription_response_result import V1getProductInfoSubscriptionResponseResult


class V1getProductInfoSubscriptionResponse(BaseModel):
    """
    object model
    """

    result: Optional[List[Optional[V1getProductInfoSubscriptionResponseResult]]] = Field(alias="result", default=None)
