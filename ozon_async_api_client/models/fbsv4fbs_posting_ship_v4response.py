from typing import *

from pydantic import BaseModel, Field


class Fbsv4fbsPostingShipV4response(BaseModel):
    """
    object model
    """

    additional_data: Optional[Any] = Field(alias="additional_data", default=None)

    result: Optional[Any] = Field(alias="result", default=None)
