from typing import *

from pydantic import BaseModel, Field

from .seller_api_product_v1response_product_deactivate import SellerApiProductV1responseProductDeactivate


class SellerApiProductV1responseResultDeactivate(BaseModel):
    """
    object model

    Результаты запроса.
    """

    product_ids: Optional[List[float]] = Field(alias="product_ids", default=None)

    rejected: Optional[List[Optional[SellerApiProductV1responseProductDeactivate]]] = Field(
        alias="rejected", default=None
    )
