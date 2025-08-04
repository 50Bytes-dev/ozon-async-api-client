from typing import *

from pydantic import BaseModel, Field


class OperationService(BaseModel):
    """
    object model
    """

    name: Optional[str] = Field(alias="name", default=None)

    price: Optional[float] = Field(alias="price", default=None)
