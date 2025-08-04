from typing import *

from pydantic import BaseModel, Field


class V1declineDiscountTasksRequestTask(BaseModel):
    """
    object model
    """

    id: int = Field(alias="id")

    seller_comment: Optional[str] = Field(alias="seller_comment", default=None)
