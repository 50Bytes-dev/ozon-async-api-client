from typing import *

from pydantic import BaseModel, Field


class Fbsv4setProductExemplarRequestProduct(BaseModel):
    """
    object model
    """

    exemplars: Optional[Any] = Field(alias="exemplars", default=None)

    product_id: Optional[int] = Field(alias="product_id", default=None)
