from typing import *

from pydantic import BaseModel, Field


class GetSupplyOrdersListRequestPaging(BaseModel):
    """
    object model

    Настройка отображения списка заявок.
    """

    from_supply_order_id: Optional[int] = Field(alias="from_supply_order_id", default=None)

    limit: int = Field(alias="limit")
