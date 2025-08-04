from typing import *

from pydantic import BaseModel, Field


class V4getProductAttributesResponsePdf(BaseModel):
    """
    object model
    """

    file_name: Optional[str] = Field(alias="file_name", default=None)

    name: Optional[str] = Field(alias="name", default=None)
