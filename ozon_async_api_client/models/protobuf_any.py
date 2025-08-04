from typing import *

from pydantic import BaseModel, Field


class ProtobufAny(BaseModel):
    """
    object model
    """

    typeUrl: Optional[str] = Field(alias="typeUrl", default=None)

    value: Optional[str] = Field(alias="value", default=None)
