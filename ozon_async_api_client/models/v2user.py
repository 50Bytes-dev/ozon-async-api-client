from typing import *

from pydantic import BaseModel, Field


class V2user(BaseModel):
    """
    object model

    Информация об участнике чата.
    """

    id: Optional[Union[str, int]] = Field(alias="id", default=None)

    type: Optional[str] = Field(alias="type", default=None)
