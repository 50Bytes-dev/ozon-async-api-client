from typing import *

from pydantic import BaseModel, Field


class V1productActionTimerUpdateRequest(BaseModel):
    """
    None model
    """

    product_ids: Optional[Any] = Field(alias="product_ids", default=None)
