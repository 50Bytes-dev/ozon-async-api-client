from typing import *

from pydantic import BaseModel, Field

from .price_indexes_index_external_data import PriceIndexesIndexExternalData
from .price_indexes_index_ozon_data import PriceIndexesIndexOzonData
from .price_indexes_index_self_data import PriceIndexesIndexSelfData


class GetProductInfoPricesResponseItemPriceIndexes(BaseModel):
    """
        object model

        Индексы цены товара.

    [Подробнее об индексе цен в Базе знаний продавца](https://seller-edu.ozon.ru/seller-rating/metrics/price-index)

    """

    color_index: Optional[str] = Field(alias="color_index", default=None)

    external_index_data: Optional[PriceIndexesIndexExternalData] = Field(alias="external_index_data", default=None)

    ozon_index_data: Optional[PriceIndexesIndexOzonData] = Field(alias="ozon_index_data", default=None)

    self_marketplaces_index_data: Optional[PriceIndexesIndexSelfData] = Field(
        alias="self_marketplaces_index_data", default=None
    )
