from typing import *

from pydantic import BaseModel, Field

from .price_indexes_color_index import PriceIndexesColorIndex
from .price_indexes_index_data_external import PriceIndexesIndexDataExternal
from .price_indexes_index_data_ozon import PriceIndexesIndexDataOzon
from .price_indexes_index_data_self import PriceIndexesIndexDataSelf


class GetProductInfoListResponsePriceIndexes(BaseModel):
    """
    object model

    Ценовые индексы товара.
    """

    color_index: Optional[PriceIndexesColorIndex] = Field(alias="color_index", default=None)

    external_index_data: Optional[PriceIndexesIndexDataExternal] = Field(alias="external_index_data", default=None)

    ozon_index_data: Optional[PriceIndexesIndexDataOzon] = Field(alias="ozon_index_data", default=None)

    self_marketplaces_index_data: Optional[PriceIndexesIndexDataSelf] = Field(
        alias="self_marketplaces_index_data", default=None
    )
