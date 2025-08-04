from typing import *

from pydantic import BaseModel, Field

from .posting_exemplar_info_exemplar_error import PostingExemplarInfoExemplarError


class UploadPostingCodesResponsePostingExemplarInfo(BaseModel):
    """
    None model
    """

    failed_exemplars: Optional[List[Optional[PostingExemplarInfoExemplarError]]] = Field(
        alias="failed_exemplars", default=None
    )

    received_qty: Optional[int] = Field(alias="received_qty", default=None)

    rejected_qty: Optional[int] = Field(alias="rejected_qty", default=None)

    sku: Optional[int] = Field(alias="sku", default=None)
