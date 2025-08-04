from typing import *

from pydantic import BaseModel, Field


class Fbsv4getProductExemplarStatusResponse(BaseModel):
    """
    object model
    """

    posting_number: Optional[str] = Field(alias="posting_number", default=None)

    products: Optional[Any] = Field(alias="products", default=None)

    status: Optional[str] = Field(alias="status", default=None)
