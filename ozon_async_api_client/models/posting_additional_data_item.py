from typing import *

from pydantic import BaseModel, Field


class PostingAdditionalDataItem(BaseModel):
    """
    None model
    """

    key: Optional[str] = Field(alias="key", default=None)

    value: Optional[str] = Field(alias="value", default=None)
