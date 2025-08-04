from typing import *

from pydantic import BaseModel, Field


class V1supplyOrderCancelResponse(BaseModel):
    """
    None model
    """

    operation_id: Optional[Union[str, int]] = Field(alias="operation_id", default=None)
