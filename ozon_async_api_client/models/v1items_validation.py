from typing import *

from pydantic import BaseModel, Field


class V1itemsValidation(BaseModel):
    """
    None model
    """

    reasons: Optional[List[str]] = Field(alias="reasons", default=None)

    sku: Optional[int] = Field(alias="sku", default=None)
