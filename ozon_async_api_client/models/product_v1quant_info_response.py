from typing import *

from pydantic import BaseModel, Field

from .product_v1quant_info_response_result_items import ProductV1quantInfoResponseResultItems


class ProductV1quantInfoResponse(BaseModel):
    """
    object model
    """

    items: Optional[List[Optional[ProductV1quantInfoResponseResultItems]]] = Field(alias="items", default=None)
