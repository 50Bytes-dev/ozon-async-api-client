from typing import *

from pydantic import BaseModel, Field


class ReportCreateDiscountedResponse(BaseModel):
    """
    object model
    """

    code: Optional[str] = Field(alias="code", default=None)
