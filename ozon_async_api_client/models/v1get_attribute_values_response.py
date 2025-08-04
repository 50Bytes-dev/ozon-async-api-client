from typing import *

from pydantic import BaseModel, Field

from .v1get_attribute_values_response_dictionary_value import V1getAttributeValuesResponseDictionaryValue


class V1getAttributeValuesResponse(BaseModel):
    """
    object model
    """

    has_next: Optional[bool] = Field(alias="has_next", default=None)

    result: Optional[List[Optional[V1getAttributeValuesResponseDictionaryValue]]] = Field(alias="result", default=None)
