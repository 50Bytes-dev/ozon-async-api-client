from typing import *

from pydantic import BaseModel, Field

from .review_info_response_photo import ReviewInfoResponsePhoto
from .review_info_response_video import ReviewInfoResponseVideo


class V1reviewInfoResponse(BaseModel):
    """
    None model
    """

    comments_amount: Optional[int] = Field(alias="comments_amount", default=None)

    dislikes_amount: Optional[int] = Field(alias="dislikes_amount", default=None)

    id: Optional[Union[str, int]] = Field(alias="id", default=None)

    is_rating_participant: Optional[bool] = Field(alias="is_rating_participant", default=None)

    likes_amount: Optional[int] = Field(alias="likes_amount", default=None)

    order_status: Optional[str] = Field(alias="order_status", default=None)

    photos: Optional[List[Optional[ReviewInfoResponsePhoto]]] = Field(alias="photos", default=None)

    photos_amount: Optional[int] = Field(alias="photos_amount", default=None)

    published_at: Optional[str] = Field(alias="published_at", default=None)

    rating: Optional[int] = Field(alias="rating", default=None)

    sku: Optional[int] = Field(alias="sku", default=None)

    status: Optional[str] = Field(alias="status", default=None)

    text: Optional[str] = Field(alias="text", default=None)

    videos: Optional[List[Optional[ReviewInfoResponseVideo]]] = Field(alias="videos", default=None)

    videos_amount: Optional[int] = Field(alias="videos_amount", default=None)
