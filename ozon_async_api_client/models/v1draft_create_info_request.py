from typing import *

from pydantic import BaseModel, Field


class V1draftCreateInfoRequest(BaseModel):
    """
    None model
    """

    operation_id: str = Field(alias="operation_id")
