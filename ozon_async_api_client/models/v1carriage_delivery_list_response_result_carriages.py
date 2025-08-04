from typing import *

from pydantic import BaseModel, Field


class V1carriageDeliveryListResponseResultCarriages(BaseModel):
    """
    object model
    """

    id: Optional[int] = Field(alias="id", default=None)

    postings_count: Optional[int] = Field(alias="postings_count", default=None)

    quantum_count: Optional[int] = Field(alias="quantum_count", default=None)

    status: Optional[str] = Field(alias="status", default=None)
