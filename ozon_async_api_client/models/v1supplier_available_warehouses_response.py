from typing import *

from pydantic import BaseModel, Field


class V1supplierAvailableWarehousesResponse(BaseModel):
    """
    object model
    """

    result: Optional[Any] = Field(alias="result", default=None)
