from typing import *

from pydantic import BaseModel, Field


class V2postingFBSActListFilter(BaseModel):
    """
    object model

    Параметры фильтра.
    """

    date_from: str = Field(alias="date_from")

    date_to: str = Field(alias="date_to")

    integration_type: Optional[str] = Field(alias="integration_type", default=None)

    status: Optional[List[str]] = Field(alias="status", default=None)
