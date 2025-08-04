from typing import *

from pydantic import BaseModel, Field

from .filter_period import FilterPeriod


class FinanceTransactionListV3requestFilter(BaseModel):
    """
    object model

    Фильтр.
    """

    date: Optional[FilterPeriod] = Field(alias="date", default=None)

    operation_type: Optional[List[str]] = Field(alias="operation_type", default=None)

    posting_number: Optional[str] = Field(alias="posting_number", default=None)

    transaction_type: Optional[str] = Field(alias="transaction_type", default=None)
