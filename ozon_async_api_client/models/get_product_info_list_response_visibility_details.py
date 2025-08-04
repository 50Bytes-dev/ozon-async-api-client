from typing import *

from pydantic import BaseModel, Field


class GetProductInfoListResponseVisibilityDetails(BaseModel):
    """
    object model

    Настройки видимости товара.
    """

    has_price: Optional[bool] = Field(alias="has_price", default=None)

    has_stock: Optional[bool] = Field(alias="has_stock", default=None)
