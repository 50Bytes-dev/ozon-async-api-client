from typing import *

from pydantic import BaseModel, Field


class ImportProductRequestPromotion(BaseModel):
    """
    object model
    """

    operation: Optional[str] = Field(alias="operation", default=None)

    type: Optional[str] = Field(alias="type", default=None)
