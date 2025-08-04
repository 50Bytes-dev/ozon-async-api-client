from typing import *

from pydantic import BaseModel, Field


class V1competitor(BaseModel):
    """
    object model
    """

    coefficient: float = Field(alias="coefficient")

    competitor_id: int = Field(alias="competitor_id")
