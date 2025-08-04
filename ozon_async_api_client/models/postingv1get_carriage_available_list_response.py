from typing import *

from pydantic import BaseModel, Field


class Postingv1getCarriageAvailableListResponse(BaseModel):
    """
    object model
    """

    result: Optional[Any] = Field(alias="result", default=None)
