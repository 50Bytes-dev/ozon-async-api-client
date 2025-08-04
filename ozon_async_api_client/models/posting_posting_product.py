from typing import *

from pydantic import BaseModel, Field


class PostingPostingProduct(BaseModel):
    """
    None model
    """

    currency_code: Optional[str] = Field(alias="currency_code", default=None)

    name: Optional[str] = Field(alias="name", default=None)

    offer_id: Optional[Union[str, int]] = Field(alias="offer_id", default=None)

    price: Optional[str] = Field(alias="price", default=None)

    required_qty_for_digital_code: Optional[int] = Field(alias="required_qty_for_digital_code", default=None)

    sku: Optional[int] = Field(alias="sku", default=None)
