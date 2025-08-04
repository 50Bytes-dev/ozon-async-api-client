from typing import *

from pydantic import BaseModel, Field


class FinanceCashFlowStatementListResponseReturnService(BaseModel):
    """
    object model

    Детализация.
    """

    name: Optional[str] = Field(alias="name", default=None)

    price: Optional[float] = Field(alias="price", default=None)
