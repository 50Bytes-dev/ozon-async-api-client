from typing import *

from pydantic import BaseModel, Field


class PostingGetFboPostingListRequestFilter(BaseModel):
    """
    object model

    Фильтр для поиска отправлений.
    """

    since: str = Field(alias="since")

    status: Optional[str] = Field(alias="status", default=None)

    to: str = Field(alias="to")
