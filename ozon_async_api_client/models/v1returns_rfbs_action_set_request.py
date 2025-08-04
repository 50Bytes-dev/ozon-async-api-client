from typing import *

from pydantic import BaseModel, Field


class V1returnsRfbsActionSetRequest(BaseModel):
    """
    None model
    """

    comment: Optional[str] = Field(alias="comment", default=None)

    compensation_amount: Optional[float] = Field(alias="compensation_amount", default=None)

    id: Optional[int] = Field(alias="id", default=None)

    rejection_reason_id: Optional[int] = Field(alias="rejection_reason_id", default=None)

    return_for_back_way: Optional[float] = Field(alias="return_for_back_way", default=None)

    return_id: Optional[int] = Field(alias="return_id", default=None)
