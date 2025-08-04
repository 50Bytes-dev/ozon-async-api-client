from typing import *

from pydantic import BaseModel, Field


class V6fbsPostingProductExemplarCreateOrGetV6request(BaseModel):
    """
    None model
    """

    posting_number: Optional[str] = Field(alias="posting_number", default=None)
