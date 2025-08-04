from typing import *

from pydantic import BaseModel, Field


class V3financeCashFlowStatementListResponseResult(BaseModel):
    """
    object model

    Результат работы метода.
    """

    cash_flows: Optional[Any] = Field(alias="cash_flows", default=None)

    details: Optional[List[Any]] = Field(alias="details", default=None)

    page_count: Optional[int] = Field(alias="page_count", default=None)
