from typing import *

from pydantic import BaseModel, Field


class CreatedAt(BaseModel):
    """
    object model

    Период создания заявки.
    """

    from_: Optional[str] = Field(alias="from", default=None)

    to: Optional[str] = Field(alias="to", default=None)
