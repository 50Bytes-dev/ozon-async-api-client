from typing import *

from pydantic import BaseModel, Field

from .v1supply_order_content_update_response_error_enum import V1supplyOrderContentUpdateResponseErrorEnum


class V1supplyOrderContentUpdateResponse(BaseModel):
    """
    None model
    """

    errors: Optional[List[Optional[V1supplyOrderContentUpdateResponseErrorEnum]]] = Field(alias="errors", default=None)

    operation_id: Optional[Union[str, int]] = Field(alias="operation_id", default=None)
