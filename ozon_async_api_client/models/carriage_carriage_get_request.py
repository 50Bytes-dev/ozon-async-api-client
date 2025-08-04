from typing import *

from pydantic import BaseModel, Field


class CarriageCarriageGetRequest(BaseModel):
    """
    None model
    """

    carriage_id: int = Field(alias="carriage_id")
