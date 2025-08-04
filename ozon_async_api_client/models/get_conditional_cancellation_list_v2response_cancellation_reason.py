from typing import *

from pydantic import BaseModel, Field


class GetConditionalCancellationListV2responseCancellationReason(BaseModel):
    """
    None model

    Причина отмены.
    """

    id: Optional[int] = Field(alias="id", default=None)

    name: Optional[str] = Field(alias="name", default=None)
