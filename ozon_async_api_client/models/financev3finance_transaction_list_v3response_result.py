from typing import *

from pydantic import BaseModel, Field

from .finance_transaction_list_v3response_operation import FinanceTransactionListV3responseOperation


class Financev3financeTransactionListV3responseResult(BaseModel):
    """
    object model

    Результаты запроса.
    """

    operations: Optional[List[Optional[FinanceTransactionListV3responseOperation]]] = Field(
        alias="operations", default=None
    )

    page_count: Optional[int] = Field(alias="page_count", default=None)

    row_count: Optional[int] = Field(alias="row_count", default=None)
