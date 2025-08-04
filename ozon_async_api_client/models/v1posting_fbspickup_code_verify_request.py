from typing import *

from pydantic import BaseModel, Field


class V1postingFBSPickupCodeVerifyRequest(BaseModel):
    """
    None model
    """

    pickup_code: str = Field(alias="pickup_code")

    posting_number: str = Field(alias="posting_number")
