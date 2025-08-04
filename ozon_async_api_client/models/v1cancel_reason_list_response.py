from typing import *

from pydantic import BaseModel, Field

from .cancel_reason_list_response_cancel_reason import CancelReasonListResponseCancelReason


class V1cancelReasonListResponse(BaseModel):
    """
    object model
    """

    result: Optional[List[Optional[CancelReasonListResponseCancelReason]]] = Field(alias="result", default=None)
