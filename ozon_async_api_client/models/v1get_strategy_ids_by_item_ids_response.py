from typing import *

from pydantic import BaseModel, Field

from .v1get_strategy_ids_by_item_ids_response_result import V1getStrategyIDsByItemIDsResponseResult


class V1getStrategyIDsByItemIDsResponse(BaseModel):
    """
    object model
    """

    result: Optional[V1getStrategyIDsByItemIDsResponseResult] = Field(alias="result", default=None)
