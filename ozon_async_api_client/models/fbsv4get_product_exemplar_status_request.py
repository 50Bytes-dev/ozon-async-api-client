from typing import *

from pydantic import BaseModel, Field


class Fbsv4getProductExemplarStatusRequest(BaseModel):
    """
    object model
    """

    posting_number: str = Field(alias="posting_number")
