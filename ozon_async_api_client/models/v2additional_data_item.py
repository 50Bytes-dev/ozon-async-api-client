from typing import *

from pydantic import BaseModel, Field


class V2additionalDataItem(BaseModel):
    """
    object model

    Дополнительная информация.
    """

    key: Optional[str] = Field(alias="key", default=None)

    value: Optional[str] = Field(alias="value", default=None)
