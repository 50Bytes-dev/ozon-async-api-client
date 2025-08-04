from typing import *

from pydantic import BaseModel, Field


class V1returnsCompanyFbsInfoRequestFilter(BaseModel):
    """
    object model

    Фильтры.
    """

    place_id: Optional[int] = Field(alias="place_id", default=None)
