from typing import *

from pydantic import BaseModel, Field

from .postingv3posting_multi_box_qty_set_v3response_result import Postingv3postingMultiBoxQtySetV3responseResult


class Postingv3postingMultiBoxQtySetV3response(BaseModel):
    """
    object model
    """

    result: Optional[Postingv3postingMultiBoxQtySetV3responseResult] = Field(alias="result", default=None)
