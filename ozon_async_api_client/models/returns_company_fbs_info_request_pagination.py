from typing import *

from pydantic import BaseModel, Field


class ReturnsCompanyFbsInfoRequestPagination(BaseModel):
    """
    object model

    Разделение ответа метода.
    """

    last_id: Optional[int] = Field(alias="last_id", default=None)

    limit: int = Field(alias="limit")
