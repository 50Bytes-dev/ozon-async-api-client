from typing import *

from pydantic import BaseModel, Field

from .get_etgb_request_date import GetEtgbRequestDate


class V1getEtgbRequest(BaseModel):
    """
    object model
    """

    date: GetEtgbRequestDate = Field(alias="date")
