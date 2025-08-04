from typing import *

from pydantic import BaseModel, Field


class ProductBooleanResponse(BaseModel):
    """
    object model
    """

    result: Optional[bool] = Field(alias="result", default=None)
