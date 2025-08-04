from typing import *

from pydantic import BaseModel, Field

from .seller_api_product_v1response_result_deactivate import SellerApiProductV1responseResultDeactivate


class SellerApiProductV1responseDeactivate(BaseModel):
    """
    object model
    """

    result: Optional[SellerApiProductV1responseResultDeactivate] = Field(alias="result", default=None)
