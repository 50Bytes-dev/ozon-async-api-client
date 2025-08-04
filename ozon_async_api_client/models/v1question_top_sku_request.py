from typing import *

from pydantic import BaseModel, Field


class V1questionTopSkuRequest(BaseModel):
    """
    object model
    """

    limit: int = Field(alias="limit")
