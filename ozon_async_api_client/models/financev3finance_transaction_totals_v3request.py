from typing import *

from pydantic import BaseModel, Field

from .finance_transaction_totals_v3request_date import FinanceTransactionTotalsV3requestDate


class Financev3financeTransactionTotalsV3request(BaseModel):
    """
    object model
    """

    date: Optional[FinanceTransactionTotalsV3requestDate] = Field(alias="date", default=None)

    posting_number: Optional[str] = Field(alias="posting_number", default=None)

    transaction_type: Optional[str] = Field(alias="transaction_type", default=None)
