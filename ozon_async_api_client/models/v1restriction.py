from typing import *

from pydantic import BaseModel, Field


class V1restriction(BaseModel):
    """
    object model
    """

    posting_number: Optional[str] = Field(alias="posting_number", default=None)

    max_posting_weight: Optional[float] = Field(alias="max_posting_weight", default=None)

    min_posting_weight: Optional[float] = Field(alias="min_posting_weight", default=None)

    width: Optional[float] = Field(alias="width", default=None)

    length: Optional[float] = Field(alias="length", default=None)

    height: Optional[float] = Field(alias="height", default=None)

    max_posting_price: Optional[float] = Field(alias="max_posting_price", default=None)

    min_posting_price: Optional[float] = Field(alias="min_posting_price", default=None)
