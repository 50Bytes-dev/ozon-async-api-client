from typing import *

from pydantic import BaseModel, Field


class V1supplyOrderCancelStatusRequest(BaseModel):
    """
    None model
    """

    operation_id: str = Field(alias="operation_id")
