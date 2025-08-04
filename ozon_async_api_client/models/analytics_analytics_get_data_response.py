from typing import *

from pydantic import BaseModel, Field

from .analytics_get_data_response_result import AnalyticsGetDataResponseResult


class AnalyticsAnalyticsGetDataResponse(BaseModel):
    """
    object model
    """

    result: Optional[AnalyticsGetDataResponseResult] = Field(alias="result", default=None)

    timestamp: Optional[str] = Field(alias="timestamp", default=None)
