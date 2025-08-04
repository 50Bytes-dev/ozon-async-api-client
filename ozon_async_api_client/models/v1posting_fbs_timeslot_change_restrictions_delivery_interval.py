from typing import *

from pydantic import BaseModel, Field


class V1postingFbsTimeslotChangeRestrictionsDeliveryInterval(BaseModel):
    """
    object model

    Период дат, доступных для переноса.
    """

    begin: Optional[str] = Field(alias="begin", default=None)

    end: Optional[str] = Field(alias="end", default=None)
