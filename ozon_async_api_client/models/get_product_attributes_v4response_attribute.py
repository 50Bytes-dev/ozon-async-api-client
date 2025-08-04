from typing import *

from pydantic import BaseModel, Field

from .get_product_attributes_v3response_dictionary_value import GetProductAttributesV3responseDictionaryValue


class GetProductAttributesV4responseAttribute(BaseModel):
    """
    object model
    """

    id: Optional[int] = Field(alias="id", default=None)

    complex_id: Optional[int] = Field(alias="complex_id", default=None)

    values: Optional[List[Optional[GetProductAttributesV3responseDictionaryValue]]] = Field(
        alias="values", default=None
    )
