from typing import *

from pydantic import BaseModel, Field

from .productv2products_stocks_request_stock import Productv2productsStocksRequestStock


class Productv2productsStocksRequest(BaseModel):
    """
    object model
    """

    stocks: List[Productv2productsStocksRequestStock] = Field(alias="stocks")
