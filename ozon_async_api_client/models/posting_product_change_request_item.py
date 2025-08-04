from typing import *

from pydantic import BaseModel, Field


class PostingProductChangeRequestItem(BaseModel):
    """
    object model
    """

    sku: int = Field(alias="sku")

    weightReal: List[float] = Field(alias="weightReal")
