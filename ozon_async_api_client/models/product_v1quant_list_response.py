from typing import *

from pydantic import BaseModel, Field


class ProductV1quantListResponse(BaseModel):
    """
    object model
    """

    cursor: Optional[str] = Field(alias="cursor", default=None)

    products: Optional[Any] = Field(alias="products", default=None)

    total_items: Optional[int] = Field(alias="total_items", default=None)
