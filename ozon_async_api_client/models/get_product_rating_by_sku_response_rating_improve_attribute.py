from typing import *

from pydantic import BaseModel, Field


class GetProductRatingBySkuResponseRatingImproveAttribute(BaseModel):
    """
    object model
    """

    id: Optional[int] = Field(alias="id", default=None)

    name: Optional[str] = Field(alias="name", default=None)
