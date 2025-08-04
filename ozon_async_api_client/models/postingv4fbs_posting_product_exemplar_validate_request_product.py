from typing import *

from pydantic import BaseModel, Field


class Postingv4fbsPostingProductExemplarValidateRequestProduct(BaseModel):
    """
    object model
    """

    exemplars: Optional[Any] = Field(alias="exemplars", default=None)

    product_id: int = Field(alias="product_id")
