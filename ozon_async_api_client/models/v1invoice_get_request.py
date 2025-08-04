from typing import *

from pydantic import BaseModel, Field


class V1invoiceGetRequest(BaseModel):
    """
    object model
    """

    posting_number: str = Field(alias="posting_number")
