from typing import *

from pydantic import BaseModel, Field


class V1draftSupplyCreateStatusRequest(BaseModel):
    """
    DraftSupplyCreateStatus model
    """

    operation_id: Union[str, int] = Field(alias="operation_id")
