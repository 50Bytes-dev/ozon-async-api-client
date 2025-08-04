from typing import *

from pydantic import BaseModel, Field


class FinanceTransactionTotalsV3requestDate(BaseModel):
    """
    object model

    Фильтр по дате.
    """

    from_: Optional[str] = Field(alias="from", default=None)

    to: Optional[str] = Field(alias="to", default=None)
