from typing import *

from pydantic import BaseModel, Field

from .fbs_posting_tracking_number_set_request_tracking_number import FbsPostingTrackingNumberSetRequestTrackingNumber


class PostingFbsPostingTrackingNumberSetRequest(BaseModel):
    """
    object model
    """

    tracking_numbers: List[FbsPostingTrackingNumberSetRequestTrackingNumber] = Field(alias="tracking_numbers")
