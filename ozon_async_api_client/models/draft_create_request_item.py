from typing import *

from pydantic import BaseModel, Field


class DraftCreateRequestItem(BaseModel):
    """
    None model
    """

    quantity: int = Field(alias="quantity")

    sku: int = Field(alias="sku")
