from typing import *

from pydantic import BaseModel, Field

from .v3import_products_request_attribute import V3importProductsRequestAttribute


class V3importProductsRequestComplexAttribute(BaseModel):
    """
    None model
    """

    attributes: Optional[List[Optional[V3importProductsRequestAttribute]]] = Field(alias="attributes", default=None)
