from typing import *

from pydantic import BaseModel, Field

from .v3import_products_request_item import V3importProductsRequestItem


class V3importProductsRequest(BaseModel):
    """
    object model
    """

    items: Optional[List[Optional[V3importProductsRequestItem]]] = Field(alias="items", default=None)
