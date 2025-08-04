from typing import *

from pydantic import BaseModel, Field


class ProductV1quantInfoResponseResultItemsQuantInfoQuantsDimensions(BaseModel):
    """
    object model

    Габариты.
    """

    depth: Optional[int] = Field(alias="depth", default=None)

    height: Optional[int] = Field(alias="height", default=None)

    weight: Optional[int] = Field(alias="weight", default=None)

    width: Optional[int] = Field(alias="width", default=None)
