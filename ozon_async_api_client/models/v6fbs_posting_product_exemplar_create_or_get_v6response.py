from typing import *

from pydantic import BaseModel, Field

from .fbs_posting_product_exemplar_create_or_get_v6response_product import \
    FbsPostingProductExemplarCreateOrGetV6responseProduct


class V6fbsPostingProductExemplarCreateOrGetV6response(BaseModel):
    """
    None model
    """

    multi_box_qty: Optional[int] = Field(alias="multi_box_qty", default=None)

    posting_number: Optional[str] = Field(alias="posting_number", default=None)

    products: Optional[List[Optional[FbsPostingProductExemplarCreateOrGetV6responseProduct]]] = Field(
        alias="products", default=None
    )
