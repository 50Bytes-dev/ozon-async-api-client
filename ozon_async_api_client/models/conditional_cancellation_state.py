from typing import *

from pydantic import BaseModel, Field


class ConditionalCancellationState(BaseModel):
    """
    object model

    Статус заявки на отмену.
    """

    id: Optional[int] = Field(alias="id", default=None)

    name: Optional[str] = Field(alias="name", default=None)

    state: Optional[str] = Field(alias="state", default=None)
