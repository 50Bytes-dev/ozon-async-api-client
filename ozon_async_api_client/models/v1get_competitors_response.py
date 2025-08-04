from typing import *

from pydantic import BaseModel, Field

from .get_competitors_response_competitor_info import GetCompetitorsResponseCompetitorInfo


class V1getCompetitorsResponse(BaseModel):
    """
    object model
    """

    competitor: Optional[List[Optional[GetCompetitorsResponseCompetitorInfo]]] = Field(alias="competitor", default=None)

    total: Optional[int] = Field(alias="total", default=None)
