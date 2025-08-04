from typing import *

from pydantic import BaseModel, Field


class V1getProductInfoDiscountedRequest(BaseModel):
    """
    object model
    """

    discounted_skus: Any = Field(alias="discounted_skus")
