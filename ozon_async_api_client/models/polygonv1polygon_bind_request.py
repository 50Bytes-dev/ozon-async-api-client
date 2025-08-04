from typing import *

from pydantic import BaseModel, Field

from .polygon_bind_requestpolygon import PolygonBindRequestpolygon
from .polygon_bind_requestwh_location import PolygonBindRequestwhLocation


class Polygonv1polygonBindRequest(BaseModel):
    """
    object model
    """

    delivery_method_id: int = Field(alias="delivery_method_id")

    polygons: List[PolygonBindRequestpolygon] = Field(alias="polygons")

    warehouse_location: PolygonBindRequestwhLocation = Field(alias="warehouse_location")
