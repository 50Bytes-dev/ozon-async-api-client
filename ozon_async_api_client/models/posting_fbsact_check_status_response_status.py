from typing import *

from pydantic import BaseModel, Field


class PostingFBSActCheckStatusResponseStatus(BaseModel):
    """
    object model

    Результат работы метода.
    """

    act_type: Optional[str] = Field(alias="act_type", default=None)

    added_to_act: Optional[List[str]] = Field(alias="added_to_act", default=None)

    removed_from_act: Optional[List[str]] = Field(alias="removed_from_act", default=None)

    status: Optional[str] = Field(alias="status", default=None)

    is_partial: Optional[bool] = Field(alias="is_partial", default=None)

    has_postings_for_next_carriage: Optional[bool] = Field(alias="has_postings_for_next_carriage", default=None)

    partial_num: Optional[int] = Field(alias="partial_num", default=None)
