from typing import *

from pydantic import BaseModel, Field


class V1productUpdateAttributesRequest(BaseModel):
    """
    object model
    """

    items: Optional[Any] = Field(alias="items", default=None)
