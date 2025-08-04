from typing import *

from pydantic import BaseModel, Field


class V3dimensions(BaseModel):
    """
    object model

    Размеры товара.
    """

    height: Optional[str] = Field(alias="height", default=None)

    length: Optional[str] = Field(alias="length", default=None)

    weight: Optional[str] = Field(alias="weight", default=None)

    width: Optional[str] = Field(alias="width", default=None)
