from typing import *

from pydantic import BaseModel, Field


class FbsPostingShipV4responseShipAdditionalData(BaseModel):
    """
    None model
    """

    posting_number: Optional[str] = Field(alias="posting_number", default=None)

    products: Optional[Any] = Field(alias="products", default=None)
