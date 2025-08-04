from typing import *

from pydantic import BaseModel, Field


class GetProductRatingBySkuResponseProductRating(BaseModel):
    """
    object model
    """

    sku: Optional[int] = Field(alias="sku", default=None)

    rating: Optional[float] = Field(alias="rating", default=None)

    groups: Optional[Any] = Field(alias="groups", default=None)
