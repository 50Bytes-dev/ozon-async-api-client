from typing import *

from pydantic import BaseModel, Field


class GetUploadQuotaResponseTotal(BaseModel):
    """
    object model

    Лимит на ассортимент.
    """

    limit: Optional[int] = Field(alias="limit", default=None)

    usage: Optional[int] = Field(alias="usage", default=None)
