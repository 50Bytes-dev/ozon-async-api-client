from typing import *

from pydantic import BaseModel, Field


class V2productInfoPicturesResponseError(BaseModel):
    """
    object model
    """

    message: Optional[str] = Field(alias="message", default=None)

    url: Optional[str] = Field(alias="url", default=None)
