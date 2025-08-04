from typing import *

from pydantic import BaseModel, Field

from .v5fbs_posting_product_exemplar_validate_v5response_product import \
    V5fbsPostingProductExemplarValidateV5responseProduct


class V5fbsPostingProductExemplarValidateV5response(BaseModel):
    """
    None model
    """

    products: Optional[List[Optional[V5fbsPostingProductExemplarValidateV5responseProduct]]] = Field(
        alias="products", default=None
    )
