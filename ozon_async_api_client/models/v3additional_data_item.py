from typing import *

from pydantic import BaseModel, Field


class V3additionalDataItem(BaseModel):
    """
    object model
    """

    key: Optional[str] = Field(alias="key", default=None)

    value: Optional[str] = Field(alias="value", default=None)
