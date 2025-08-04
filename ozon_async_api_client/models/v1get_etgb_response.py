from typing import *

from pydantic import BaseModel, Field

from .get_etgb_response_result import GetEtgbResponseResult


class V1getEtgbResponse(BaseModel):
    """
    object model
    """

    result: Optional[List[Optional[GetEtgbResponseResult]]] = Field(alias="result", default=None)
