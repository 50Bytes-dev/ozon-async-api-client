from typing import *

from pydantic import BaseModel, Field


class AddStrategyItemsResponseError(BaseModel):
    """
    object model
    """

    code: Optional[str] = Field(alias="code", default=None)

    error: Optional[str] = Field(alias="error", default=None)

    product_id: Optional[int] = Field(alias="product_id", default=None)
