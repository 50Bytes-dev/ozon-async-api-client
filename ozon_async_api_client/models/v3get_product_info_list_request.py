from typing import *

from pydantic import BaseModel, Field


class V3getProductInfoListRequest(BaseModel):
    """
    object model
    """

    offer_id: Optional[List[str]] = Field(alias="offer_id", default=None)

    product_id: Optional[List[int]] = Field(alias="product_id", default=None)

    sku: Optional[List[int]] = Field(alias="sku", default=None)
