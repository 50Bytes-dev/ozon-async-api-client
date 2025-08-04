from typing import *

from pydantic import BaseModel, Field

from .v5fbs_posting_product_exemplar_create_or_get_v5response_product_exemplar import \
    V5fbsPostingProductExemplarCreateOrGetV5responseProductExemplar


class V5fbsPostingProductExemplarCreateOrGetV5responseProduct(BaseModel):
    """
    None model
    """

    exemplars: Optional[List[Optional[V5fbsPostingProductExemplarCreateOrGetV5responseProductExemplar]]] = Field(
        alias="exemplars", default=None
    )

    is_gtd_needed: Optional[bool] = Field(alias="is_gtd_needed", default=None)

    is_mandatory_mark_needed: Optional[bool] = Field(alias="is_mandatory_mark_needed", default=None)

    is_rnpt_needed: Optional[bool] = Field(alias="is_rnpt_needed", default=None)

    product_id: Optional[int] = Field(alias="product_id", default=None)

    quantity: Optional[int] = Field(alias="quantity", default=None)
