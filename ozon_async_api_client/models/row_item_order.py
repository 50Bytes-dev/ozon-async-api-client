from typing import *

from pydantic import BaseModel, Field


class RowItemOrder(BaseModel):
    """
    object model

    Информация о заказе.
    """

    posting_number: Optional[str] = Field(alias="posting_number", default=None)

    created_date: Optional[str] = Field(alias="created_date", default=None)
