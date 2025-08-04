from typing import *

from pydantic import BaseModel, Field

from .created_at import CreatedAt


class V2returnsRfbsFilter(BaseModel):
    """
    object model

    Фильтр.
    """

    offer_id: Optional[Union[str, int]] = Field(alias="offer_id", default=None)

    posting_number: Optional[str] = Field(alias="posting_number", default=None)

    group_state: Optional[List[str]] = Field(alias="group_state", default=None)

    created_at: Optional[CreatedAt] = Field(alias="created_at", default=None)
