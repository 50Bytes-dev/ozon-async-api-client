from typing import *

from pydantic import BaseModel, Field

from .v5fbs_posting_product_exemplar_set_v5request_product_exemplar import \
    V5fbsPostingProductExemplarSetV5requestProductExemplar


class V5fbsPostingProductExemplarSetV5requestProduct(BaseModel):
    """
    None model
    """

    exemplars: Optional[List[Optional[V5fbsPostingProductExemplarSetV5requestProductExemplar]]] = Field(
        alias="exemplars", default=None
    )

    is_gtd_needed: Optional[bool] = Field(alias="is_gtd_needed", default=None)

    is_mandatory_mark_needed: Optional[bool] = Field(alias="is_mandatory_mark_needed", default=None)

    is_rnpt_needed: Optional[bool] = Field(alias="is_rnpt_needed", default=None)

    product_id: int = Field(alias="product_id")

    quantity: Optional[int] = Field(alias="quantity", default=None)
