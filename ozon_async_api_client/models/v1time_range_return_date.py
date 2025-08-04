from typing import *

from pydantic import BaseModel, Field


class V1timeRangeReturnDate(BaseModel):
    """
    object model

    Фильтр по дате создания возврата.
    """

    time_from: Optional[str] = Field(alias="time_from", default=None)

    time_to: Optional[str] = Field(alias="time_to", default=None)
