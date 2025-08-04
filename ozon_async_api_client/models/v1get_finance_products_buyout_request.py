from typing import *

from pydantic import BaseModel, Field


class V1getFinanceProductsBuyoutRequest(BaseModel):
    """
    None model
    """

    date_from: str = Field(alias="date_from")

    date_to: str = Field(alias="date_to")
