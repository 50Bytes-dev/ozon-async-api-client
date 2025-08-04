from typing import *

from pydantic import BaseModel, Field

from .filter_op import FilterOp


class AnalyticsFilter(BaseModel):
    """
    object model
    """

    key: Optional[str] = Field(alias="key", default=None)

    op: Optional[FilterOp] = Field(alias="op", default=None)

    value: Optional[str] = Field(alias="value", default=None)
