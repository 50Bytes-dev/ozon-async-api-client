from typing import *

from pydantic import BaseModel, Field


class RowItem(BaseModel):
    """
    object model

    Информация о товаре.
    """

    barcode: Optional[str] = Field(alias="barcode", default=None)

    name: Optional[str] = Field(alias="name", default=None)

    offer_id: Optional[Union[str, int]] = Field(alias="offer_id", default=None)

    sku: Optional[int] = Field(alias="sku", default=None)
