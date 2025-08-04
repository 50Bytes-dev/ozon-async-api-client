from typing import *

from pydantic import BaseModel, Field


class V2returnsRfbsReturnMoneyRequest(BaseModel):
    """
    object model
    """

    return_id: int = Field(alias="return_id")

    return_for_back_way: Optional[int] = Field(alias="return_for_back_way", default=None)
