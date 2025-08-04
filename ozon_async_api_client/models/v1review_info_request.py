from typing import *

from pydantic import BaseModel, Field


class V1reviewInfoRequest(BaseModel):
    """
    ReviewInfo model
    """

    review_id: str = Field(alias="review_id")
