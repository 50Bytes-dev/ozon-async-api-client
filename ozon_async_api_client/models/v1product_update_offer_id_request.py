from typing import *

from pydantic import BaseModel, Field


class V1productUpdateOfferIdRequest(BaseModel):
    """
    object model
    """

    update_offer_id: Any = Field(alias="update_offer_id")
