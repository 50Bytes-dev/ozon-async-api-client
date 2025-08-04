from typing import *

from pydantic import BaseModel, Field

from .v5fbs_posting_product_exemplar_validate_v5request_product import \
    V5fbsPostingProductExemplarValidateV5requestProduct


class V5fbsPostingProductExemplarValidateV5request(BaseModel):
    """
    None model
    """

    posting_number: Optional[str] = Field(alias="posting_number", default=None)

    products: Optional[List[Optional[V5fbsPostingProductExemplarValidateV5requestProduct]]] = Field(
        alias="products", default=None
    )
