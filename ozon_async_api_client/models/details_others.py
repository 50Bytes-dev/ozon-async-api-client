from typing import *

from pydantic import BaseModel, Field

from .finance_cash_flow_statement_list_response_details_others import FinanceCashFlowStatementListResponseDetailsOthers


class DetailsOthers(BaseModel):
    """
    object model

    Компенсация и прочие начисления.
    """

    total: Optional[float] = Field(alias="total", default=None)

    items: Optional[List[Optional[FinanceCashFlowStatementListResponseDetailsOthers]]] = Field(
        alias="items", default=None
    )
