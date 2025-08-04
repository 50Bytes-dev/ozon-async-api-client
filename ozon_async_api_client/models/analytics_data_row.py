from typing import *

from pydantic import BaseModel, Field

from .analytics_data_row_dimension import AnalyticsDataRowDimension


class AnalyticsDataRow(BaseModel):
    """
    object model
    """

    dimensions: Optional[List[Optional[AnalyticsDataRowDimension]]] = Field(alias="dimensions", default=None)

    metrics: Optional[List[float]] = Field(alias="metrics", default=None)
