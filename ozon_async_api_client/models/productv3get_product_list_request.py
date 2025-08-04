from typing import *

from pydantic import BaseModel, Field

from .productv3get_product_list_request_filter import Productv3getProductListRequestFilter


class Productv3getProductListRequest(BaseModel):
    """
    object model
    """

    filter: Optional[Productv3getProductListRequestFilter] = Field(alias="filter", default=None)

    last_id: Optional[Union[str, int]] = Field(alias="last_id", default=None)

    limit: Optional[int] = Field(alias="limit", default=None)
