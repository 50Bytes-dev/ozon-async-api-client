from typing import *

from pydantic import BaseModel, Field

from .draft_create_request_item import DraftCreateRequestItem
from .v1create_type import V1createType


class V1draftCreateRequest(BaseModel):
    """
    DraftCreate messages model
    """

    cluster_ids: Optional[List[int]] = Field(alias="cluster_ids", default=None)

    drop_off_point_warehouse_id: Optional[int] = Field(alias="drop_off_point_warehouse_id", default=None)

    items: List[DraftCreateRequestItem] = Field(alias="items")

    type: V1createType = Field(alias="type")
