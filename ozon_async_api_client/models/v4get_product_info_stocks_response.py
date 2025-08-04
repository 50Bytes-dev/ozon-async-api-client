from typing import *

from pydantic import BaseModel, Field

from .v4get_product_info_stocks_response_item import V4getProductInfoStocksResponseItem


class V4getProductInfoStocksResponse(BaseModel):
    """
    None model
    """

    cursor: Optional[str] = Field(alias="cursor", default=None)

    items: Optional[List[Optional[V4getProductInfoStocksResponseItem]]] = Field(alias="items", default=None)

    total: Optional[int] = Field(alias="total", default=None)
