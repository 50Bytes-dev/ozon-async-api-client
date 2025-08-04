from typing import *

from pydantic import BaseModel, Field


class V2hsCode(BaseModel):
    """
    object model
    """

    code: Optional[str] = Field(alias="code", default=None)

    sku: Optional[Union[str, int]] = Field(alias="sku", default=None)
