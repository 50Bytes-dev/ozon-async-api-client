from typing import *

from pydantic import BaseModel, Field


class ProductProductUnarchiveRequest(BaseModel):
    """
    object model
    """

    product_id: List[int] = Field(alias="product_id")
