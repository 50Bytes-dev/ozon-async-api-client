from typing import *

from pydantic import BaseModel, Field


class V5fbsPostingProductExemplarCreateOrGetV5request(BaseModel):
    """
    None model
    """

    posting_number: str = Field(alias="posting_number")
