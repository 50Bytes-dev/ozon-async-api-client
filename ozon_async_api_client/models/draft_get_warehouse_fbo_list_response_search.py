from typing import *

from pydantic import BaseModel, Field

from .draft_get_warehouse_fbo_list_response_coordinate import DraftGetWarehouseFboListResponseCoordinate
from .draft_get_warehouse_fbo_list_response_warehouse_type import DraftGetWarehouseFboListResponseWarehouseType


class DraftGetWarehouseFboListResponseSearch(BaseModel):
    """
    None model
    """

    address: Optional[str] = Field(alias="address", default=None)

    coordinates: Optional[DraftGetWarehouseFboListResponseCoordinate] = Field(alias="coordinates", default=None)

    name: Optional[str] = Field(alias="name", default=None)

    warehouse_id: Optional[int] = Field(alias="warehouse_id", default=None)

    warehouse_type: Optional[DraftGetWarehouseFboListResponseWarehouseType] = Field(
        alias="warehouse_type", default=None
    )
