from typing import *

from pydantic import BaseModel, Field


class V1getSupplyOrderTimeslotStatusRequest(BaseModel):
    """
    object model
    """

    operation_id: str = Field(alias="operation_id")
