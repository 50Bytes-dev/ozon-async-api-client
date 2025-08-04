from typing import *

from pydantic import BaseModel, Field


class V1supplyOrderPassStatusRequest(BaseModel):
    """
    object model
    """

    operation_id: Union[str, int] = Field(alias="operation_id")
