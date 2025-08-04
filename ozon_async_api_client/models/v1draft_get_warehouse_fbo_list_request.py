from typing import *

from pydantic import BaseModel, Field

from .v1create_type import V1createType


class V1draftGetWarehouseFboListRequest(BaseModel):
    """
    DraftGetWarehouseFboList model
    """

    filter_by_supply_type: List[V1createType] = Field(alias="filter_by_supply_type")

    search: str = Field(alias="search")
