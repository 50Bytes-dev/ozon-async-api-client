from typing import *

from pydantic import BaseModel, Field


class GetConditionalCancellationListV2requestWith(BaseModel):
    """
    None model

    Дополнительная информация.
    """

    counter: Optional[bool] = Field(alias="counter", default=None)
