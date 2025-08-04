from typing import *

from pydantic import BaseModel, Field

from .upload_posting_codes_response_posting_exemplar_info import UploadPostingCodesResponsePostingExemplarInfo


class V1uploadPostingCodesResponse(BaseModel):
    """
    None model
    """

    exemplars_by_sku: Optional[List[Optional[UploadPostingCodesResponsePostingExemplarInfo]]] = Field(
        alias="exemplars_by_sku", default=None
    )
