from typing import *

from pydantic import BaseModel, Field


class V1questionTopSkuResponse(BaseModel):
    """
    object model
    """

    sku: Optional[Any] = Field(alias="sku", default=None)
