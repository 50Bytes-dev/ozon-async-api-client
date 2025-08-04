from typing import *

from pydantic import BaseModel, Field

from .v5fbs_posting_product_exemplar_validate_v5response_product_exemplar import \
    V5fbsPostingProductExemplarValidateV5responseProductExemplar


class V5fbsPostingProductExemplarValidateV5responseProduct(BaseModel):
    """
    None model
    """

    error: Optional[str] = Field(alias="error", default=None)

    exemplars: Optional[List[Optional[V5fbsPostingProductExemplarValidateV5responseProductExemplar]]] = Field(
        alias="exemplars", default=None
    )

    product_id: Optional[int] = Field(alias="product_id", default=None)

    valid: Optional[bool] = Field(alias="valid", default=None)
