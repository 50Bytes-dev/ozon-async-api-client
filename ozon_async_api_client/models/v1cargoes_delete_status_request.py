from typing import *

from pydantic import BaseModel, Field


class V1cargoesDeleteStatusRequest(BaseModel):
    """
    None model
    """

    operation_id: Optional[str] = Field(alias="operation_id", default=None)
