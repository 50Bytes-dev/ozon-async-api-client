from typing import *

from pydantic import BaseModel, Field

from .product_import_products_by_skurequest_item import ProductImportProductsBySKURequestItem


class ProductImportProductsBySKURequest(BaseModel):
    """
    object model
    """

    items: Optional[List[Optional[ProductImportProductsBySKURequestItem]]] = Field(alias="items", default=None)
