from typing import *

from pydantic import BaseModel, Field


class V1draftSupplyCreateStatusRequest(BaseModel):
    """
    DraftSupplyCreateStatus model
    """

    operation_id: str = Field(alias="operation_id")
