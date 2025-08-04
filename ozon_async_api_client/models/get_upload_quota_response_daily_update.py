from typing import *

from pydantic import BaseModel, Field


class GetUploadQuotaResponseDailyUpdate(BaseModel):
    """
    object model

    Суточный лимит на обновление товаров.
    """

    limit: Optional[int] = Field(alias="limit", default=None)

    reset_at: Optional[str] = Field(alias="reset_at", default=None)

    usage: Optional[int] = Field(alias="usage", default=None)
