from typing import *

from pydantic import BaseModel, Field


class DraftGetWarehouseFboListResponseCoordinate(BaseModel):
    """
    None model

    Координаты склада.
    """

    latitude: Optional[float] = Field(alias="latitude", default=None)

    longitude: Optional[float] = Field(alias="longitude", default=None)
