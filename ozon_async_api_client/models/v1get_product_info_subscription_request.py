from typing import *

from pydantic import BaseModel, Field


class V1getProductInfoSubscriptionRequest(BaseModel):
    """
    object model
    """

    skus: List[str] = Field(alias="skus")
