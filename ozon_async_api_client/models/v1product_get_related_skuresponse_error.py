from typing import *

from pydantic import BaseModel, Field


class V1productGetRelatedSKUResponseError(BaseModel):
    """
    object model
    """

    code: Optional[str] = Field(alias="code", default=None)

    sku: Optional[int] = Field(alias="sku", default=None)

    message: Optional[str] = Field(alias="message", default=None)
