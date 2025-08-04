from typing import *

from pydantic import BaseModel, Field


class V4fbsPostingShipPackageV4response(BaseModel):
    """
    None model
    """

    result: Optional[str] = Field(alias="result", default=None)
