from typing import *

from pydantic import BaseModel, Field


class V1productUpdateOfferIdResponseError(BaseModel):
    """
    object model
    """

    message: Optional[str] = Field(alias="message", default=None)

    offer_id: Optional[str] = Field(alias="offer_id", default=None)
