from typing import *

from pydantic import BaseModel, Field


class V1draftCreateResponse(BaseModel):
    """
    None model
    """

    operation_id: Optional[str] = Field(alias="operation_id", default=None)
