from typing import *

from pydantic import BaseModel, Field


class V1productUpdateDiscountRequest(BaseModel):
    """
    object model
    """

    discount: int = Field(alias="discount")

    product_id: int = Field(alias="product_id")
