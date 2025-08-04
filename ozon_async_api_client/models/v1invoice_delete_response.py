from typing import *

from pydantic import BaseModel, Field


class V1invoiceDeleteResponse(BaseModel):
    """
    object model
    """

    result: Optional[bool] = Field(alias="result", default=None)
