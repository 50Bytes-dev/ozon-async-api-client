from typing import *

from pydantic import BaseModel, Field

from .seller_api_product_v1response_result import SellerApiProductV1responseResult


class SellerApiProductV1response(BaseModel):
    """
    object model
    """

    result: Optional[SellerApiProductV1responseResult] = Field(alias="result", default=None)
