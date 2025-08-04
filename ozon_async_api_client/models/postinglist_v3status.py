from typing import *

from pydantic import BaseModel, Field


class PostinglistV3status(BaseModel):
    """
    object model

    Период, в который последний раз изменялся статус у отправлений.
    """

    from_: Optional[str] = Field(alias="from", default=None)

    to: Optional[str] = Field(alias="to", default=None)
