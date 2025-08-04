from typing import *

from pydantic import BaseModel, Field


class ListPostingCodesRequestFilter(BaseModel):
    """
    None model

    Фильтр для поиска отправлений.
    """

    posting_number: Optional[List[str]] = Field(alias="posting_number", default=None)

    since: Optional[str] = Field(alias="since", default=None)

    to: Optional[str] = Field(alias="to", default=None)
