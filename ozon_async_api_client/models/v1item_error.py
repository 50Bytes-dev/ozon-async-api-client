from typing import *

from pydantic import BaseModel, Field


class V1itemError(BaseModel):
    """
    object model
    """

    code: Optional[str] = Field(alias="code", default=None)

    message: Optional[str] = Field(alias="message", default=None)

    state: Optional[str] = Field(alias="state", default=None)

    level: Optional[str] = Field(alias="level", default=None)

    description: Optional[str] = Field(alias="description", default=None)

    field: Optional[str] = Field(alias="field", default=None)

    attribute_id: Optional[int] = Field(alias="attribute_id", default=None)

    attribute_name: Optional[str] = Field(alias="attribute_name", default=None)
