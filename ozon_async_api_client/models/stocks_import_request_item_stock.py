from typing import *

from pydantic import BaseModel, Field


class StocksImportRequestItemStock(BaseModel):
    """
    None model
    """

    offer_id: str = Field(alias="offer_id")

    stock: int = Field(alias="stock")
