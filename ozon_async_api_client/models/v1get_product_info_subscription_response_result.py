from typing import *

from pydantic import BaseModel, Field


class V1getProductInfoSubscriptionResponseResult(BaseModel):
    """
    object model
    """

    count: Optional[int] = Field(alias="count", default=None)

    sku: Optional[int] = Field(alias="sku", default=None)
