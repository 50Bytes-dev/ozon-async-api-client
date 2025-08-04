from typing import *

from pydantic import BaseModel, Field


class V3financeCashFlowStatementListResponsePeriod(BaseModel):
    """
    object model

    Период.
    """

    begin: Optional[str] = Field(alias="begin", default=None)

    end: Optional[str] = Field(alias="end", default=None)

    id: Optional[int] = Field(alias="id", default=None)
