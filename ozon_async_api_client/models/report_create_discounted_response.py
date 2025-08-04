from typing import *

from pydantic import BaseModel, Field


class ReportCreateDiscountedResponse(BaseModel):
    """
    object model
    """

    code: Optional[Union[str, int]] = Field(alias="code", default=None)
