from typing import *

from pydantic import BaseModel, Field

from .get_returns_list_response_visual_status import GetReturnsListResponseVisualStatus


class GetReturnsListResponseVisual(BaseModel):
    """
    object model

    Информация о статусе возврата.
    """

    status: Optional[GetReturnsListResponseVisualStatus] = Field(alias="status", default=None)

    change_moment: Optional[str] = Field(alias="change_moment", default=None)
