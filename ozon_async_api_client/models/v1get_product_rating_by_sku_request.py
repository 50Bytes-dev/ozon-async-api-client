from typing import *

from pydantic import BaseModel, Field


class V1getProductRatingBySkuRequest(BaseModel):
    """
    object model
    """

    skus: Any = Field(alias="skus")
