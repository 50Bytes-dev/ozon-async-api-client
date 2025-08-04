from typing import *

from pydantic import BaseModel, Field


class SupplierAvailableWarehousesResponseCapacity(BaseModel):
    """
    object model
    """

    start: Optional[str] = Field(alias="start", default=None)

    end: Optional[str] = Field(alias="end", default=None)

    value: Optional[int] = Field(alias="value", default=None)
