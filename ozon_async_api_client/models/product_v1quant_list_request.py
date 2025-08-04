from typing import *

from pydantic import BaseModel, Field


class ProductV1quantListRequest(BaseModel):
    """
    object model
    """

    cursor: Optional[str] = Field(alias="cursor", default=None)

    limit: Optional[int] = Field(alias="limit", default=None)

    visibility: Optional[str] = Field(alias="visibility", default=None)
