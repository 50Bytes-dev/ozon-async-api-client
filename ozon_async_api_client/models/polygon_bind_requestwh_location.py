from typing import *

from pydantic import BaseModel, Field


class PolygonBindRequestwhLocation(BaseModel):
    """
    object model

    Расположение склада.
    """

    lat: str = Field(alias="lat")

    lon: str = Field(alias="lon")
