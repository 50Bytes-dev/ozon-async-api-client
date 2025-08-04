from typing import *

from pydantic import BaseModel, Field


class GetReturnsListResponseAdditionalInfo(BaseModel):
    """
    object model

    Дополнительная информация.
    """

    is_opened: Optional[bool] = Field(alias="is_opened", default=None)

    is_super_econom: Optional[bool] = Field(alias="is_super_econom", default=None)
