from typing import *

from pydantic import BaseModel, Field

from .v5fbs_posting_product_exemplar_set_v5request_product import V5fbsPostingProductExemplarSetV5requestProduct


class V5fbsPostingProductExemplarSetV5request(BaseModel):
    """
    None model
    """

    multi_box_qty: Optional[int] = Field(alias="multi_box_qty", default=None)

    posting_number: str = Field(alias="posting_number")

    products: List[V5fbsPostingProductExemplarSetV5requestProduct] = Field(alias="products")
