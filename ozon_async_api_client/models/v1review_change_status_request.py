from typing import *

from pydantic import BaseModel, Field


class V1reviewChangeStatusRequest(BaseModel):
    """
    ReviewChangeStatus model
    """

    review_ids: List[str] = Field(alias="review_ids")

    status: str = Field(alias="status")
