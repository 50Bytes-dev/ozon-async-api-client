from typing import *

from pydantic import BaseModel, Field

from .finance_transaction_list_v3request_filter import FinanceTransactionListV3requestFilter


class Financev3financeTransactionListV3request(BaseModel):
    """
    object model
    """

    filter: Optional[FinanceTransactionListV3requestFilter] = Field(alias="filter", default=None)

    page: int = Field(alias="page")

    page_size: int = Field(alias="page_size")
