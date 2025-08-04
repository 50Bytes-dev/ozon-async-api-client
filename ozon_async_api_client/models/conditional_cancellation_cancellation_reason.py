from typing import *

from pydantic import BaseModel, Field


class ConditionalCancellationCancellationReason(BaseModel):
    """
    object model

    Причина отмены.
    """

    id: Optional[int] = Field(alias="id", default=None)

    name: Optional[str] = Field(alias="name", default=None)
