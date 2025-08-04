from typing import *

from pydantic import BaseModel, Field


class RatingSummaryV1responseLocalIndex(BaseModel):
    """
    None model
    """

    calculation_date: Optional[str] = Field(alias="calculation_date", default=None)

    localization_percentage: Optional[int] = Field(alias="localization_percentage", default=None)
