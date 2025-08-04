from typing import *

from pydantic import BaseModel, Field


class PolygonBindRequestpolygon(BaseModel):
    """
    object model
    """

    polygon_id: int = Field(alias="polygon_id")

    time: int = Field(alias="time")
