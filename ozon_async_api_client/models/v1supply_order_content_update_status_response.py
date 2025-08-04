from typing import *

from pydantic import BaseModel, Field

from .supply_order_content_update_status_response_status_enum import SupplyOrderContentUpdateStatusResponseStatusEnum
from .v1supply_order_content_update_status_response_error_enum import V1supplyOrderContentUpdateStatusResponseErrorEnum


class V1supplyOrderContentUpdateStatusResponse(BaseModel):
    """
    None model
    """

    errors: Optional[List[Optional[V1supplyOrderContentUpdateStatusResponseErrorEnum]]] = Field(
        alias="errors", default=None
    )

    status: Optional[SupplyOrderContentUpdateStatusResponseStatusEnum] = Field(alias="status", default=None)
