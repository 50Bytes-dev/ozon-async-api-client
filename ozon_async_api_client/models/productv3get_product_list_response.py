from typing import *

from pydantic import BaseModel, Field

from .productv3get_product_list_response_result import Productv3getProductListResponseResult


class Productv3getProductListResponse(BaseModel):
    """
    object model
    """

    result: Optional[Productv3getProductListResponseResult] = Field(alias="result", default=None)
