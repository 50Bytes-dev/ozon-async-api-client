from typing import *

from pydantic import BaseModel, Field


class V5fbsPostingProductExemplarStatusV5request(BaseModel):
    """
    None model
    """

    posting_number: Optional[str] = Field(alias="posting_number", default=None)
