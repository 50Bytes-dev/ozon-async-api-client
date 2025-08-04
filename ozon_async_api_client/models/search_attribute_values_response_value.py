from typing import *

from pydantic import BaseModel, Field


class SearchAttributeValuesResponseValue(BaseModel):
    """
    object model
    """

    id: Optional[int] = Field(alias="id", default=None)

    info: Optional[str] = Field(alias="info", default=None)

    picture: Optional[str] = Field(alias="picture", default=None)

    value: Optional[str] = Field(alias="value", default=None)
