from typing import *

from pydantic import BaseModel, Field


class FbsPostingTrackingNumberSetRequestTrackingNumber(BaseModel):
    """
    object model
    """

    posting_number: str = Field(alias="posting_number")

    tracking_number: str = Field(alias="tracking_number")
