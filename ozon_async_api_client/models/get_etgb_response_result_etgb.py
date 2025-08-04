from typing import *

from pydantic import BaseModel, Field


class GetEtgbResponseResultEtgb(BaseModel):
    """
    object model

    Информация о декларации.
    """

    number: Optional[str] = Field(alias="number", default=None)

    date: Optional[str] = Field(alias="date", default=None)

    url: Optional[str] = Field(alias="url", default=None)
