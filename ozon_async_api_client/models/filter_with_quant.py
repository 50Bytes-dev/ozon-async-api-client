from typing import *

from pydantic import BaseModel, Field


class FilterWithQuant(BaseModel):
    """
    None model

    Товары по тарифу «Эконом».
    """

    created: Optional[bool] = Field(alias="created", default=None)

    exists: Optional[bool] = Field(alias="exists", default=None)
