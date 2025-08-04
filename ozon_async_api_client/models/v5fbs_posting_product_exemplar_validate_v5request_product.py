from typing import *

from pydantic import BaseModel, Field

from .v5fbs_posting_product_exemplar_validate_v5request_product_exemplar import \
    V5fbsPostingProductExemplarValidateV5requestProductExemplar


class V5fbsPostingProductExemplarValidateV5requestProduct(BaseModel):
    """
    None model
    """

    exemplars: Optional[List[Optional[V5fbsPostingProductExemplarValidateV5requestProductExemplar]]] = Field(
        alias="exemplars", default=None
    )

    product_id: Optional[int] = Field(alias="product_id", default=None)
