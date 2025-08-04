from typing import *

from pydantic import BaseModel, Field

from .productv3get_product_list_response_item_quant import Productv3getProductListResponseItemQuant


class Productv3getProductListResponseItem(BaseModel):
    """
    object model
    """

    archived: Optional[bool] = Field(alias="archived", default=None)

    has_fbo_stocks: Optional[bool] = Field(alias="has_fbo_stocks", default=None)

    has_fbs_stocks: Optional[bool] = Field(alias="has_fbs_stocks", default=None)

    is_discounted: Optional[bool] = Field(alias="is_discounted", default=None)

    offer_id: Optional[str] = Field(alias="offer_id", default=None)

    product_id: Optional[int] = Field(alias="product_id", default=None)

    quants: Optional[Productv3getProductListResponseItemQuant] = Field(alias="quants", default=None)
