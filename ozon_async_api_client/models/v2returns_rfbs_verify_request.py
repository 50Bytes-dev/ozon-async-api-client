from typing import *

from pydantic import BaseModel, Field


class V2returnsRfbsVerifyRequest(BaseModel):
    """
    object model
    """

    return_id: int = Field(alias="return_id")

    return_method_description: Optional[str] = Field(alias="return_method_description", default=None)
