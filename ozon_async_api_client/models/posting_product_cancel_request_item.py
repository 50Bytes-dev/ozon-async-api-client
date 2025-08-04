from typing import *

from pydantic import BaseModel, Field


class PostingProductCancelRequestItem(BaseModel):
    """
    object model
    """

    quantity: int = Field(alias="quantity")

    sku: int = Field(alias="sku")
