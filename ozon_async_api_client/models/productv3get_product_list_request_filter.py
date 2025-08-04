from typing import *

from pydantic import BaseModel, Field

from .productv3get_product_list_request_filter_filter_visibility import \
    Productv3getProductListRequestFilterFilterVisibility


class Productv3getProductListRequestFilter(BaseModel):
    """
    object model

    Фильтр по товарам.
    """

    offer_id: Optional[Any] = Field(alias="offer_id", default=None)

    product_id: Optional[Any] = Field(alias="product_id", default=None)

    visibility: Optional[Productv3getProductListRequestFilterFilterVisibility] = Field(alias="visibility", default=None)
