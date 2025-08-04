from typing import *

from pydantic import BaseModel, Field

from .seller_api_product import SellerApiProduct


class SellerApiGetSellerProductV1responseResult(BaseModel):
    """
    object model

    Результаты запроса.
    """

    products: Optional[List[Optional[SellerApiProduct]]] = Field(alias="products", default=None)

    total: Optional[float] = Field(alias="total", default=None)

    last_id: Optional[float] = Field(alias="last_id", default=None)
