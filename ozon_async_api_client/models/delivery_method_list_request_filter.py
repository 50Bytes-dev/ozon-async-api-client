from typing import *

from pydantic import BaseModel, Field


class DeliveryMethodListRequestFilter(BaseModel):
    """
    object model

    Фильтр для поиска методов доставки.
    """

    provider_id: Optional[int] = Field(alias="provider_id", default=None)

    status: Optional[str] = Field(alias="status", default=None)

    warehouse_id: Optional[int] = Field(alias="warehouse_id", default=None)
