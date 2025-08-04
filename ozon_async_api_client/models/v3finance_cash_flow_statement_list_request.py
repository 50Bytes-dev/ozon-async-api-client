from typing import *

from pydantic import BaseModel, Field

from .financev3period import Financev3period


class V3financeCashFlowStatementListRequest(BaseModel):
    """
    object model
    """

    date: Financev3period = Field(alias="date")

    page: int = Field(alias="page")

    with_details: Optional[bool] = Field(alias="with_details", default=None)

    page_size: int = Field(alias="page_size")
