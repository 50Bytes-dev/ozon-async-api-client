from typing import *

from pydantic import BaseModel, Field

from .details_returns import DetailsReturns


class DetailsReturnDetails(BaseModel):
    """
    object model

    Возвраты и отмены.
    """

    total: Optional[float] = Field(alias="total", default=None)

    amount: Optional[float] = Field(alias="amount", default=None)

    return_services: Optional[DetailsReturns] = Field(alias="return_services", default=None)
