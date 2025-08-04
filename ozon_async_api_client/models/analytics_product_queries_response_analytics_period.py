from typing import *

from pydantic import BaseModel, Field


class AnalyticsProductQueriesResponseAnalyticsPeriod(BaseModel):
    """
    None model

    Период, за который формируется аналитика.
    """

    date_from: Optional[str] = Field(alias="date_from", default=None)

    date_to: Optional[str] = Field(alias="date_to", default=None)
