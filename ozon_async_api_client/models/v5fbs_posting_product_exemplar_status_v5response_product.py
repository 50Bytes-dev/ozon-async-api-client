from typing import *

from pydantic import BaseModel, Field

from .v5fbs_posting_product_exemplar_status_v5response_product_exemplar import \
    V5fbsPostingProductExemplarStatusV5responseProductExemplar


class V5fbsPostingProductExemplarStatusV5responseProduct(BaseModel):
    """
    None model
    """

    exemplars: Optional[List[Optional[V5fbsPostingProductExemplarStatusV5responseProductExemplar]]] = Field(
        alias="exemplars", default=None
    )

    product_id: Optional[int] = Field(alias="product_id", default=None)
