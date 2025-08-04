from typing import *

from pydantic import BaseModel, Field


class SupplierAvailableWarehousesResponseSchedule(BaseModel):
    """
    object model

    Загруженность.
    """

    capacity: Optional[Any] = Field(alias="capacity", default=None)

    date: Optional[str] = Field(alias="date", default=None)
