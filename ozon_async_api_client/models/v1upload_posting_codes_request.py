from typing import *

from pydantic import BaseModel, Field

from .upload_posting_codes_request_posting_line_exemplar_info import UploadPostingCodesRequestPostingLineExemplarInfo


class V1uploadPostingCodesRequest(BaseModel):
    """
    None model
    """

    exemplars_by_sku: Optional[List[Optional[UploadPostingCodesRequestPostingLineExemplarInfo]]] = Field(
        alias="exemplars_by_sku", default=None
    )

    posting_number: Optional[str] = Field(alias="posting_number", default=None)
