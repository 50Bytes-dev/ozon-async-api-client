from typing import *

from pydantic import BaseModel, Field


class V1getSupplyReturnsSummaryReportRequest(BaseModel):
    """
    None model
    """

    date_from: str = Field(alias="date_from")

    date_to: str = Field(alias="date_to")

    last_id: Optional[Union[str, int]] = Field(alias="last_id", default=None)

    limit: int = Field(alias="limit")
