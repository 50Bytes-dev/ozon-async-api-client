from typing import *

from pydantic import BaseModel, Field


class GetConditionalCancellationListRequestWith(BaseModel):
    """
    object model

    Дополнительная информация.
    """

    counters: Optional[bool] = Field(alias="counters", default=None)
