from typing import *

from pydantic import BaseModel, Field

from .get_conditional_cancellation_list_v2response_result import GetConditionalCancellationListV2responseResult


class V2getConditionalCancellationListV2response(BaseModel):
    """
    None model
    """

    counter: Optional[int] = Field(alias="counter", default=None)

    last_id: Optional[int] = Field(alias="last_id", default=None)

    result: Optional[List[Optional[GetConditionalCancellationListV2responseResult]]] = Field(
        alias="result", default=None
    )
