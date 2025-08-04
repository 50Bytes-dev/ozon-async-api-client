from typing import *

from pydantic import BaseModel, Field

from .draft_get_warehouse_fbo_list_response_search import DraftGetWarehouseFboListResponseSearch


class V1draftGetWarehouseFboListResponse(BaseModel):
    """
    None model
    """

    search: Optional[List[Optional[DraftGetWarehouseFboListResponseSearch]]] = Field(alias="search", default=None)
