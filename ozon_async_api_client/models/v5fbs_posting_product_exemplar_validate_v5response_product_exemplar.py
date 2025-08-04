from typing import *

from pydantic import BaseModel, Field

from .v5fbs_posting_product_exemplar_validate_v5response_product_exemplar_mark import \
    V5fbsPostingProductExemplarValidateV5responseProductExemplarMark


class V5fbsPostingProductExemplarValidateV5responseProductExemplar(BaseModel):
    """
    None model
    """

    errors: Optional[List[str]] = Field(alias="errors", default=None)

    gtd: Optional[str] = Field(alias="gtd", default=None)

    marks: Optional[List[Optional[V5fbsPostingProductExemplarValidateV5responseProductExemplarMark]]] = Field(
        alias="marks", default=None
    )

    rnpt: Optional[str] = Field(alias="rnpt", default=None)

    valid: Optional[bool] = Field(alias="valid", default=None)
