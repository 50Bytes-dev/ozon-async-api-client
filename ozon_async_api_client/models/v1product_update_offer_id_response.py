from typing import *

from pydantic import BaseModel, Field


class V1productUpdateOfferIdResponse(BaseModel):
    """
    object model
    """

    errors: Optional[Any] = Field(alias="errors", default=None)
