from typing import *

from pydantic import BaseModel, Field


class ProductV1quantInfoRequest(BaseModel):
    """
    object model
    """

    quant_code: Any = Field(alias="quant_code")
