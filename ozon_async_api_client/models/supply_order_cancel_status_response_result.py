from typing import *

from pydantic import BaseModel, Field

from .supply_order_cancel_status_response_cancel_supply_results import \
    SupplyOrderCancelStatusResponseCancelSupplyResults


class SupplyOrderCancelStatusResponseResult(BaseModel):
    """
    None model

    Информация об отмене заявки на поставку.
    """

    is_order_cancelled: Optional[bool] = Field(alias="is_order_cancelled", default=None)

    supplies: Optional[List[Optional[SupplyOrderCancelStatusResponseCancelSupplyResults]]] = Field(
        alias="supplies", default=None
    )
