from typing import *

from pydantic import BaseModel, Field

from .review_list_response_review import ReviewListResponseReview


class V1reviewListResponse(BaseModel):
    """
    None model
    """

    has_next: Optional[bool] = Field(alias="has_next", default=None)

    last_id: Optional[str] = Field(alias="last_id", default=None)

    reviews: Optional[List[Optional[ReviewListResponseReview]]] = Field(alias="reviews", default=None)
