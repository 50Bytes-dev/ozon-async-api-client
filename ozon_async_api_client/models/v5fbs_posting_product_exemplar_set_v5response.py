from typing import *

from pydantic import BaseModel, Field


class V5fbsPostingProductExemplarSetV5response(BaseModel):
    """
    None model
    """

    result: Optional[bool] = Field(alias="result", default=None)
