from typing import *

from pydantic import BaseModel, Field


class V2movePostingToAwaitingDeliveryRequest(BaseModel):
    """
    object model
    """

    posting_number: List[str] = Field(alias="posting_number")
