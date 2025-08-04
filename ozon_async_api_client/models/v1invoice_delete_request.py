from typing import *

from pydantic import BaseModel, Field


class V1invoiceDeleteRequest(BaseModel):
    """
    object model
    """

    posting_number: str = Field(alias="posting_number")
