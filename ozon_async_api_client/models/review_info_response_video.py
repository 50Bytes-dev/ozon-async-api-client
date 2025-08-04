from typing import *

from pydantic import BaseModel, Field


class ReviewInfoResponseVideo(BaseModel):
    """
    None model
    """

    height: Optional[int] = Field(alias="height", default=None)

    preview_url: Optional[str] = Field(alias="preview_url", default=None)

    short_video_preview_url: Optional[str] = Field(alias="short_video_preview_url", default=None)

    url: Optional[str] = Field(alias="url", default=None)

    width: Optional[int] = Field(alias="width", default=None)
