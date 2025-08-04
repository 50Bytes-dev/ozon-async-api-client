from typing import *

from pydantic import BaseModel, Field


class ExemplarMark(BaseModel):
    """
    None model
    """

    mark: Optional[str] = Field(alias="mark", default=None)

    mark_type: Optional[str] = Field(alias="mark_type", default=None)
