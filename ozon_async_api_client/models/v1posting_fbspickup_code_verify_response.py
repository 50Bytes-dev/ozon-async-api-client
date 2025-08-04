from typing import *

from pydantic import BaseModel, Field


class V1postingFBSPickupCodeVerifyResponse(BaseModel):
    """
    None model
    """

    valid: Optional[bool] = Field(alias="valid", default=None)
