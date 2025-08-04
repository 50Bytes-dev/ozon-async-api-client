from typing import *

from pydantic import BaseModel, Field


class V2returnsRfbsCompensateRequest(BaseModel):
    """
    object model
    """

    compensation_amount: Optional[str] = Field(alias="compensation_amount", default=None)

    return_id: int = Field(alias="return_id")
