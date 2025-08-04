from typing import *

from pydantic import BaseModel, Field


class OperationItem(BaseModel):
    """
    object model
    """

    name: Optional[str] = Field(alias="name", default=None)

    sku: Optional[int] = Field(alias="sku", default=None)
