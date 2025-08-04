from typing import *

from pydantic import BaseModel, Field

from .product_v1quant_info_response_result_items_quant_info import ProductV1quantInfoResponseResultItemsQuantInfo


class ProductV1quantInfoResponseResultItems(BaseModel):
    """
    object model
    """

    offer_id: Optional[str] = Field(alias="offer_id", default=None)

    product_id: Optional[int] = Field(alias="product_id", default=None)

    quant_info: Optional[ProductV1quantInfoResponseResultItemsQuantInfo] = Field(alias="quant_info", default=None)
