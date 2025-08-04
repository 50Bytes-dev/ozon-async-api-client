from typing import *

from pydantic import BaseModel, Field

from .v1comment_sort import V1commentSort


class V1commentListRequest(BaseModel):
    """
    None model
    """

    limit: int = Field(alias="limit")

    offset: Optional[int] = Field(alias="offset", default=None)

    review_id: str = Field(alias="review_id")

    sort_dir: Optional[V1commentSort] = Field(alias="sort_dir", default=None)
