from typing import *

from pydantic import BaseModel, Field


class V1timeRangeStorageTariffication(BaseModel):
    """
    object model

    Фильтр по дате начала тарификации.
    """

    time_from: Optional[str] = Field(alias="time_from", default=None)

    time_to: Optional[str] = Field(alias="time_to", default=None)
