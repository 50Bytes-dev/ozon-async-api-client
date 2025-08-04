from typing import *

from pydantic import BaseModel, Field

from .product_exemplar import ProductExemplar


class FbsPostingProductExemplarCreateOrGetV6responseProduct(BaseModel):
    """
    None model
    """

    exemplars: Optional[List[Optional[ProductExemplar]]] = Field(alias="exemplars", default=None)

    is_gtd_needed: Optional[bool] = Field(alias="is_gtd_needed", default=None)

    is_jw_uin_needed: Optional[bool] = Field(alias="is_jw_uin_needed", default=None)

    is_mandatory_mark_needed: Optional[bool] = Field(alias="is_mandatory_mark_needed", default=None)

    is_mandatory_mark_possible: Optional[bool] = Field(alias="is_mandatory_mark_possible", default=None)

    is_rnpt_needed: Optional[bool] = Field(alias="is_rnpt_needed", default=None)

    product_id: Optional[int] = Field(alias="product_id", default=None)

    quantity: Optional[int] = Field(alias="quantity", default=None)
