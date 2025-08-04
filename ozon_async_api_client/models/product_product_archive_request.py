from typing import *

from pydantic import BaseModel, Field


class ProductProductArchiveRequest(BaseModel):
    """
    object model
    """

    product_id: List[int] = Field(alias="product_id")
