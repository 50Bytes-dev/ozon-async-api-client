from typing import *

from pydantic import BaseModel, Field

from .v3get_product_info_list_response_item import V3getProductInfoListResponseItem


class V3getProductInfoListResponse(BaseModel):
    """
    object model
    """

    items: Optional[List[Optional[V3getProductInfoListResponseItem]]] = Field(alias="items", default=None)
