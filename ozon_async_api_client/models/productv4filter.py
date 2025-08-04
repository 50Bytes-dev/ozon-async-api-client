from typing import *

from pydantic import BaseModel, Field

from .productv2get_product_list_request_filter_filter_visibility import \
    Productv2getProductListRequestFilterFilterVisibility


class Productv4filter(BaseModel):
    """
    object model

    Фильтр по товарам.
    """

    offer_id: Optional[Any] = Field(alias="offer_id", default=None)

    product_id: Optional[Any] = Field(alias="product_id", default=None)

    sku: Optional[List[str]] = Field(alias="sku", default=None)

    visibility: Optional[Productv2getProductListRequestFilterFilterVisibility] = Field(alias="visibility", default=None)
