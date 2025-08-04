from typing import *

from pydantic import BaseModel, Field

from .v1restriction import V1restriction


class V1getRestrictionsResponse(BaseModel):
    """
    object model
    """

    result: Optional[V1restriction] = Field(alias="result", default=None)
