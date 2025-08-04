from typing import *

from pydantic import BaseModel, Field


class V1cargoesCreateInfoRequest(BaseModel):
    """
    None model
    """

    operation_id: str = Field(alias="operation_id")
