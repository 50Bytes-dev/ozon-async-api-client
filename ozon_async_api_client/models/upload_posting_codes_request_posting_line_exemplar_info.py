from typing import *

from pydantic import BaseModel, Field


class UploadPostingCodesRequestPostingLineExemplarInfo(BaseModel):
    """
    None model
    """

    exemplar_keys: Optional[List[str]] = Field(alias="exemplar_keys", default=None)

    exemplar_qty: int = Field(alias="exemplar_qty")

    not_available_exemplar_qty: int = Field(alias="not_available_exemplar_qty")

    sku: int = Field(alias="sku")
