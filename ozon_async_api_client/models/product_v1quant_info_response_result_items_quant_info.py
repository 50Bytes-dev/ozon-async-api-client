from typing import *

from pydantic import BaseModel, Field


class ProductV1quantInfoResponseResultItemsQuantInfo(BaseModel):
    """
    object model

    Информация о кванте.
    """

    quants: Optional[Any] = Field(alias="quants", default=None)
