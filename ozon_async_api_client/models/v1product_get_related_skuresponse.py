from typing import *

from pydantic import BaseModel, Field


class V1productGetRelatedSKUResponse(BaseModel):
    """
    object model
    """

    items: Optional[Any] = Field(alias="items", default=None)

    errors: Optional[Any] = Field(alias="errors", default=None)
