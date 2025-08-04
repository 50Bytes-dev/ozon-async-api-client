from typing import *

from pydantic import BaseModel, Field

from .productv2products_stocks_response_error import Productv2productsStocksResponseError


class Productv2productsStocksResponseResult(BaseModel):
    """
    object model
    """

    errors: Optional[List[Optional[Productv2productsStocksResponseError]]] = Field(alias="errors", default=None)

    offer_id: Optional[Union[str, int]] = Field(alias="offer_id", default=None)

    product_id: Optional[int] = Field(alias="product_id", default=None)

    updated: Optional[bool] = Field(alias="updated", default=None)

    warehouse_id: Optional[int] = Field(alias="warehouse_id", default=None)
