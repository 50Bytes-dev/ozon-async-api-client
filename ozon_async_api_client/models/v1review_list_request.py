from typing import *

from pydantic import BaseModel, Field


class V1reviewListRequest(BaseModel):
    """
    ReviewList model
    """

    last_id: Optional[str] = Field(alias="last_id", default=None)

    limit: int = Field(alias="limit")

    sort_dir: Optional[str] = Field(alias="sort_dir", default=None)

    status: Optional[str] = Field(alias="status", default=None)
