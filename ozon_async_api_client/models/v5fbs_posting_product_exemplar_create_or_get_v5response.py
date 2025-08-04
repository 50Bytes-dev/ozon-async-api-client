from typing import *

from pydantic import BaseModel, Field

from .v5fbs_posting_product_exemplar_create_or_get_v5response_product import \
    V5fbsPostingProductExemplarCreateOrGetV5responseProduct


class V5fbsPostingProductExemplarCreateOrGetV5response(BaseModel):
    """
    None model
    """

    multi_box_qty: Optional[int] = Field(alias="multi_box_qty", default=None)

    posting_number: Optional[str] = Field(alias="posting_number", default=None)

    products: Optional[List[Optional[V5fbsPostingProductExemplarCreateOrGetV5responseProduct]]] = Field(
        alias="products", default=None
    )
