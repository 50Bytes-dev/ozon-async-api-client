from typing import *

from pydantic import BaseModel, Field

from .fbs_posting_product_exemplar_set_v6request_products import FbsPostingProductExemplarSetV6requestProducts


class V6fbsPostingProductExemplarSetV6request(BaseModel):
    """
    None model
    """

    multi_box_qty: Optional[int] = Field(alias="multi_box_qty", default=None)

    posting_number: Optional[str] = Field(alias="posting_number", default=None)

    products: Optional[List[Optional[FbsPostingProductExemplarSetV6requestProducts]]] = Field(
        alias="products", default=None
    )
