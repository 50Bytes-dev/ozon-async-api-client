from typing import *

from pydantic import BaseModel, Field

from .analytics_data_row import AnalyticsDataRow


class AnalyticsGetDataResponseResult(BaseModel):
    """
    object model

    Результаты запроса.
    """

    data: Optional[List[Optional[AnalyticsDataRow]]] = Field(alias="data", default=None)

    totals: Optional[List[float]] = Field(alias="totals", default=None)
