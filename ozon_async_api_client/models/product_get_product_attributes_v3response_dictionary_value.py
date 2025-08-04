from typing import *

from pydantic import BaseModel, Field


class ProductGetProductAttributesV3responseDictionaryValue(BaseModel):
    """
    object model
    """

    dictionary_value_id: Optional[int] = Field(alias="dictionary_value_id", default=None)

    value: Optional[str] = Field(alias="value", default=None)
