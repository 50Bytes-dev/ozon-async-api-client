from typing import *

from pydantic import BaseModel, Field


class V1timeRangeVisualStatus(BaseModel):
    """
    object model

    Фильтр по дате изменения статуса возврата.
    """

    time_from: Optional[str] = Field(alias="time_from", default=None)

    time_to: Optional[str] = Field(alias="time_to", default=None)
