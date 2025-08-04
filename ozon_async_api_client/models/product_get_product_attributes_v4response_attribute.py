from typing import *

from pydantic import BaseModel, Field

from .product_get_product_attributes_v3response_dictionary_value import \
    ProductGetProductAttributesV3responseDictionaryValue


class ProductGetProductAttributesV4responseAttribute(BaseModel):
    """
    object model
    """

    id: Optional[int] = Field(alias="id", default=None)

    complex_id: Optional[int] = Field(alias="complex_id", default=None)

    values: Optional[List[Optional[ProductGetProductAttributesV3responseDictionaryValue]]] = Field(
        alias="values", default=None
    )
