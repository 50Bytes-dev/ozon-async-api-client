from typing import *

from pydantic import BaseModel, Field


class V1getProductRatingBySkuResponse(BaseModel):
    """
    object model
    """

    products: Optional[Any] = Field(alias="products", default=None)
