from typing import *

from pydantic import BaseModel, Field

from .item_status_error import ItemStatusError


class StocksImportResponseItemStatus(BaseModel):
    """
    None model
    """

    errors: Optional[List[Optional[ItemStatusError]]] = Field(alias="errors", default=None)

    offer_id: Optional[Union[str, int]] = Field(alias="offer_id", default=None)

    product_id: Optional[int] = Field(alias="product_id", default=None)

    sku: Optional[int] = Field(alias="sku", default=None)

    updated: Optional[bool] = Field(alias="updated", default=None)
