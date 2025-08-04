from typing import *

from pydantic import BaseModel, Field


class StocksImportRequestItemStock(BaseModel):
    """
    None model
    """

    offer_id: Union[str, int] = Field(alias="offer_id")

    stock: int = Field(alias="stock")
