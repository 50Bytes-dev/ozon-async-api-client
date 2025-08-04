from typing import *

from pydantic import BaseModel, Field

from .v2cancellation_state_enum import V2cancellationStateEnum


class GetConditionalCancellationListV2responseState(BaseModel):
    """
    None model

    Статус заявки на отмену.
    """

    id: Optional[int] = Field(alias="id", default=None)

    name: Optional[str] = Field(alias="name", default=None)

    state: Optional[V2cancellationStateEnum] = Field(alias="state", default=None)
