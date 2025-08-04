from typing import *

from pydantic import BaseModel, Field


class ReturnsCompanyFbsInfoResponsePassInfo(BaseModel):
    """
    object model

    Информация о пропуске.
    """

    count: Optional[int] = Field(alias="count", default=None)

    is_required: Optional[bool] = Field(alias="is_required", default=None)
