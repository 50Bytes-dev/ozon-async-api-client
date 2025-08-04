from typing import *

from pydantic import BaseModel, Field


class V1itemIDsRequest(BaseModel):
    """
    object model
    """

    product_id: List[str] = Field(alias="product_id")
