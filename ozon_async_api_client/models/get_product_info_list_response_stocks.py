from typing import *

from pydantic import BaseModel, Field

from .get_product_info_list_response_stocks_stock import GetProductInfoListResponseStocksStock


class GetProductInfoListResponseStocks(BaseModel):
    """
    object model

    Информация об остатках товара.
    """

    has_stock: Optional[bool] = Field(alias="has_stock", default=None)

    stocks: Optional[List[Optional[GetProductInfoListResponseStocksStock]]] = Field(alias="stocks", default=None)
