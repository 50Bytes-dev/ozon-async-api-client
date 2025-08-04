from typing import *

from pydantic import BaseModel, Field


class Fbsv4setProductExemplarResponse(BaseModel):
    """
    object model
    """

    result: Optional[bool] = Field(alias="result", default=None)
