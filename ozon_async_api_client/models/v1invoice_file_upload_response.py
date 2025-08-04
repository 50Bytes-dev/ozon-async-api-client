from typing import *

from pydantic import BaseModel, Field


class V1invoiceFileUploadResponse(BaseModel):
    """
    object model
    """

    url: Optional[str] = Field(alias="url", default=None)
