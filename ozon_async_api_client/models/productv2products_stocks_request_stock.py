from typing import *

from pydantic import BaseModel, Field


class Productv2productsStocksRequestStock(BaseModel):
    """
    object model
    """

    offer_id: Optional[Union[str, int]] = Field(alias="offer_id", default=None)

    product_id: int = Field(alias="product_id")

    stock: int = Field(alias="stock")

    warehouse_id: int = Field(alias="warehouse_id")
