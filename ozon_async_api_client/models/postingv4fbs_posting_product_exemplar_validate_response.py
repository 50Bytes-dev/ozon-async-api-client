from typing import *

from pydantic import BaseModel, Field

from .fbs_posting_product_exemplar_validate_response_fbs_posting_product_exemplar_validate_result import \
    FbsPostingProductExemplarValidateResponseFbsPostingProductExemplarValidateResult


class Postingv4fbsPostingProductExemplarValidateResponse(BaseModel):
    """
    object model
    """

    result: Optional[FbsPostingProductExemplarValidateResponseFbsPostingProductExemplarValidateResult] = Field(
        alias="result", default=None
    )
