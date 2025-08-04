from typing import *

from pydantic import BaseModel, Field


class DeleteProductsResponseDeleteStatus(BaseModel):
    """
    object model
    """

    error: Optional[str] = Field(alias="error", default=None)

    is_deleted: Optional[bool] = Field(alias="is_deleted", default=None)

    offer_id: Optional[str] = Field(alias="offer_id", default=None)
