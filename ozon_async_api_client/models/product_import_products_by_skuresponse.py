from typing import *

from pydantic import BaseModel, Field

from .product_import_products_by_skuresponse_result import ProductImportProductsBySKUResponseResult


class ProductImportProductsBySKUResponse(BaseModel):
    """
    object model
    """

    result: Optional[ProductImportProductsBySKUResponseResult] = Field(alias="result", default=None)
