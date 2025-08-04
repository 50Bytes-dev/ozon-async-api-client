from typing import *

from pydantic import BaseModel, Field

from .fbs_posting_product_exemplar_set_v6request_exemplars import FbsPostingProductExemplarSetV6requestExemplars


class FbsPostingProductExemplarSetV6requestProducts(BaseModel):
    """
    None model
    """

    exemplars: Optional[List[Optional[FbsPostingProductExemplarSetV6requestExemplars]]] = Field(
        alias="exemplars", default=None
    )

    product_id: Optional[int] = Field(alias="product_id", default=None)
