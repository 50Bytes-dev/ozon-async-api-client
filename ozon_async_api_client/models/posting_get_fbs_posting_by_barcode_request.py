from typing import *

from pydantic import BaseModel, Field


class PostingGetFbsPostingByBarcodeRequest(BaseModel):
    """
    object model
    """

    barcode: Optional[str] = Field(alias="barcode", default=None)
