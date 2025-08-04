from typing import *

from pydantic import BaseModel, Field

from .filter_with_quant import FilterWithQuant
from .v4visibility import V4visibility


class V4getProductInfoStocksRequestFilter(BaseModel):
    """
    None model

    Фильтр по товарам.
    """

    offer_id: Optional[List[str]] = Field(alias="offer_id", default=None)

    product_id: Optional[List[str]] = Field(alias="product_id", default=None)

    visibility: Optional[V4visibility] = Field(alias="visibility", default=None)

    with_quant: Optional[FilterWithQuant] = Field(alias="with_quant", default=None)
