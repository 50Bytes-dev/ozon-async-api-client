from typing import *

from pydantic import BaseModel, Field


class V1dayTimeSlot(BaseModel):
    """
    None model

    Таймслот поставки.
    """

    from_in_timezone: Optional[str] = Field(alias="from_in_timezone", default=None)

    to_in_timezone: Optional[str] = Field(alias="to_in_timezone", default=None)
