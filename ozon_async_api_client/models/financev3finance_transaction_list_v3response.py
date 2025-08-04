from typing import *

from pydantic import BaseModel, Field

from .financev3finance_transaction_list_v3response_result import Financev3financeTransactionListV3responseResult


class Financev3financeTransactionListV3response(BaseModel):
    """
    object model
    """

    result: Optional[Financev3financeTransactionListV3responseResult] = Field(alias="result", default=None)
