from typing import *

from pydantic import BaseModel, Field

from .cancel_supply_results_cancel_supply_error import CancelSupplyResultsCancelSupplyError


class SupplyOrderCancelStatusResponseCancelSupplyResults(BaseModel):
    """
    None model
    """

    error_reasons: Optional[List[Optional[CancelSupplyResultsCancelSupplyError]]] = Field(
        alias="error_reasons", default=None
    )

    is_supply_cancelled: Optional[bool] = Field(alias="is_supply_cancelled", default=None)

    supply_id: Optional[int] = Field(alias="supply_id", default=None)
