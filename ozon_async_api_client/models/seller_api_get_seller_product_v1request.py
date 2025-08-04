from typing import *

from pydantic import BaseModel, Field


class SellerApiGetSellerProductV1request(BaseModel):
    """
    object model

    Список товаров.
    """

    action_id: float = Field(alias="action_id")

    limit: Optional[float] = Field(alias="limit", default=None)

    offset: float = Field(alias="offset")

    last_id: Optional[float] = Field(alias="last_id", default=None)
