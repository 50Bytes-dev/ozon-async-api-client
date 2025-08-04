from typing import *

from pydantic import BaseModel, Field


class Postingv4fbsPostingProductExemplarValidateRequest(BaseModel):
    """
    object model
    """

    posting_number: Optional[str] = Field(alias="posting_number", default=None)

    products: Optional[Any] = Field(alias="products", default=None)
