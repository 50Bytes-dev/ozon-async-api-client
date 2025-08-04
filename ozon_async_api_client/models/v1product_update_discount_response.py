from typing import *

from pydantic import BaseModel, Field


class V1productUpdateDiscountResponse(BaseModel):
    """
    object model
    """

    result: Optional[bool] = Field(alias="result", default=None)
