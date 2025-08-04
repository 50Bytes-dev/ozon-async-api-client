from typing import *

from pydantic import BaseModel, Field

from .search_attribute_values_response_value import SearchAttributeValuesResponseValue


class V1searchAttributeValuesResponse(BaseModel):
    """
    object model
    """

    result: Optional[List[Optional[SearchAttributeValuesResponseValue]]] = Field(alias="result", default=None)
