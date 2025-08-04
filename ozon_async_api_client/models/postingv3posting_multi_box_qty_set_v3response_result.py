from typing import *

from pydantic import BaseModel, Field


class Postingv3postingMultiBoxQtySetV3responseResult(BaseModel):
    """
    object model

    Результат передачи количества коробок.
    """

    result: Optional[bool] = Field(alias="result", default=None)
