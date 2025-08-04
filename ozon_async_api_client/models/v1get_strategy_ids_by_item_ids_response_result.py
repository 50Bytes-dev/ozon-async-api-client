from typing import *

from pydantic import BaseModel, Field

from .get_strategy_ids_by_item_ids_response_product_info import GetStrategyIDsByItemIDsResponseProductInfo


class V1getStrategyIDsByItemIDsResponseResult(BaseModel):
    """
    object model

    Результат работы метода.
    """

    products_info: Optional[List[Optional[GetStrategyIDsByItemIDsResponseProductInfo]]] = Field(
        alias="products_info", default=None
    )
