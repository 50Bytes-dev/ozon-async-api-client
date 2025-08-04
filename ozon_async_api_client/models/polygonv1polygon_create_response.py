from typing import *

from pydantic import BaseModel, Field


class Polygonv1polygonCreateResponse(BaseModel):
    """
    object model
    """

    polygon_id: Optional[int] = Field(alias="polygon_id", default=None)
