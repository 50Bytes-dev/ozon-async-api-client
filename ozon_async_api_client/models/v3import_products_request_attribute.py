from typing import *

from pydantic import BaseModel, Field

from .v3import_products_request_dictionary_value import V3importProductsRequestDictionaryValue


class V3importProductsRequestAttribute(BaseModel):
    """
    object model
    """

    complex_id: Optional[int] = Field(alias="complex_id", default=None)

    id: Optional[int] = Field(alias="id", default=None)

    values: Optional[List[Optional[V3importProductsRequestDictionaryValue]]] = Field(alias="values", default=None)
