from typing import *

from pydantic import BaseModel, Field


class Polygonv1polygonCreateRequest(BaseModel):
    """
    object model
    """

    coordinates: str = Field(alias="coordinates")
