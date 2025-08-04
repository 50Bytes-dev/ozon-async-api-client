from typing import *

from pydantic import BaseModel, Field

from .get_product_info_stocks_response_stock import GetProductInfoStocksResponseStock


class V4getProductInfoStocksResponseItem(BaseModel):
    """
    None model
    """

    offer_id: Optional[str] = Field(alias="offer_id", default=None)

    product_id: Optional[int] = Field(alias="product_id", default=None)

    stocks: Optional[List[Optional[GetProductInfoStocksResponseStock]]] = Field(alias="stocks", default=None)
