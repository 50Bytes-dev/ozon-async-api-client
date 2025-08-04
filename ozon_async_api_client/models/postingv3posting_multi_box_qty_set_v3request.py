from typing import *

from pydantic import BaseModel, Field


class Postingv3postingMultiBoxQtySetV3request(BaseModel):
    """
    object model
    """

    posting_number: str = Field(alias="posting_number")

    multi_box_qty: int = Field(alias="multi_box_qty")
