from typing import *

from pydantic import BaseModel, Field

from .v5fbs_posting_product_exemplar_status_v5response_product import V5fbsPostingProductExemplarStatusV5responseProduct


class V5fbsPostingProductExemplarStatusV5response(BaseModel):
    """
    None model
    """

    posting_number: Optional[str] = Field(alias="posting_number", default=None)

    products: Optional[List[Optional[V5fbsPostingProductExemplarStatusV5responseProduct]]] = Field(
        alias="products", default=None
    )

    status: Optional[str] = Field(alias="status", default=None)
