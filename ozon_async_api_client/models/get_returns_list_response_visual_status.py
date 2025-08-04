from typing import *

from pydantic import BaseModel, Field


class GetReturnsListResponseVisualStatus(BaseModel):
    """
    object model

    Статус возврата.
    """

    id: Optional[int] = Field(alias="id", default=None)

    display_name: Optional[str] = Field(alias="display_name", default=None)

    sys_name: Optional[str] = Field(alias="sys_name", default=None)
