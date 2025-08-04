from typing import *

from pydantic import BaseModel, Field


class V1invoiceFileUploadRequest(BaseModel):
    """
    object model
    """

    base64_content: str = Field(alias="base64_content")

    posting_number: str = Field(alias="posting_number")
