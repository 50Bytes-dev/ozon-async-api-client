from typing import *

from pydantic import BaseModel, Field

from .supply_order_cancel_status_response_cancel_order_error import SupplyOrderCancelStatusResponseCancelOrderError
from .supply_order_cancel_status_response_result import SupplyOrderCancelStatusResponseResult
from .v1supply_order_cancel_status_response_status import V1supplyOrderCancelStatusResponseStatus


class V1supplyOrderCancelStatusResponse(BaseModel):
    """
    None model
    """

    error_reasons: Optional[List[Optional[SupplyOrderCancelStatusResponseCancelOrderError]]] = Field(
        alias="error_reasons", default=None
    )

    result: Optional[SupplyOrderCancelStatusResponseResult] = Field(alias="result", default=None)

    status: Optional[V1supplyOrderCancelStatusResponseStatus] = Field(alias="status", default=None)
