from typing import *

from pydantic import BaseModel, Field

from .financev3finance_transaction_totals_v3response_result import Financev3financeTransactionTotalsV3responseResult


class Financev3financeTransactionTotalsV3response(BaseModel):
    """
    object model
    """

    result: Optional[Financev3financeTransactionTotalsV3responseResult] = Field(alias="result", default=None)
