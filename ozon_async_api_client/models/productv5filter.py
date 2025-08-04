from typing import *

from pydantic import BaseModel, Field

from .productv5get_product_list_request_filter_filter_visibility import \
    Productv5getProductListRequestFilterFilterVisibility


class Productv5filter(BaseModel):
    """
    object model

    Фильтр по товарам.
    """

    offer_id: Optional[Any] = Field(alias="offer_id", default=None)

    product_id: Optional[Any] = Field(alias="product_id", default=None)

    visibility: Optional[Productv5getProductListRequestFilterFilterVisibility] = Field(alias="visibility", default=None)
