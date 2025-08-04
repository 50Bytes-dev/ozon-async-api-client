from typing import *

from pydantic import BaseModel, Field

from .v5fbs_posting_product_exemplar_validate_v5request_product_exemplar_mark import \
    V5fbsPostingProductExemplarValidateV5requestProductExemplarMark


class V5fbsPostingProductExemplarValidateV5requestProductExemplar(BaseModel):
    """
    None model
    """

    gtd: Optional[str] = Field(alias="gtd", default=None)

    marks: Optional[List[Optional[V5fbsPostingProductExemplarValidateV5requestProductExemplarMark]]] = Field(
        alias="marks", default=None
    )

    rnpt: Optional[str] = Field(alias="rnpt", default=None)
