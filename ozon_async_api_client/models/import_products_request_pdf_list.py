from typing import *

from pydantic import BaseModel, Field


class ImportProductsRequestPdfList(BaseModel):
    """
    object model
    """

    index: Optional[int] = Field(alias="index", default=None)

    name: Optional[str] = Field(alias="name", default=None)

    src_url: Optional[str] = Field(alias="src_url", default=None)
