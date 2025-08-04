from typing import *

from pydantic import BaseModel, Field


class GetProductAttributesV3responseDictionaryValue(BaseModel):
    """
    object model
    """

    dictionaryValueId: Optional[int] = Field(alias="dictionaryValueId", default=None)

    value: Optional[str] = Field(alias="value", default=None)
