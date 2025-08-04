from typing import *

from pydantic import BaseModel, Field

from .seller_api_get_seller_product_v1response_result import SellerApiGetSellerProductV1responseResult


class SellerApiGetSellerProductV1response(BaseModel):
    """
    object model
    """

    result: Optional[SellerApiGetSellerProductV1responseResult] = Field(alias="result", default=None)
