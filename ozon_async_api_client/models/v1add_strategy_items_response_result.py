from typing import *

from pydantic import BaseModel, Field

from .add_strategy_items_response_error import AddStrategyItemsResponseError


class V1addStrategyItemsResponseResult(BaseModel):
    """
    object model

    Результат работы метода.
    """

    errors: Optional[List[Optional[AddStrategyItemsResponseError]]] = Field(alias="errors", default=None)

    failed_product_count: Optional[int] = Field(alias="failed_product_count", default=None)
