from typing import *

from pydantic import BaseModel, Field


class DeleteProductsRequestProduct(BaseModel):
    """
    object model
    """

    offer_id: Union[str, int] = Field(alias="offer_id")
