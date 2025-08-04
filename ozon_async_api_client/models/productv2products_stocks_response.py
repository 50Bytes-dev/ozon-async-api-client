from typing import *

from pydantic import BaseModel, Field

from .productv2products_stocks_response_result import Productv2productsStocksResponseResult


class Productv2productsStocksResponse(BaseModel):
    """
    object model

    Результаты запроса.
    """

    result: Optional[List[Optional[Productv2productsStocksResponseResult]]] = Field(alias="result", default=None)
