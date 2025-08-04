from typing import *

from pydantic import BaseModel, Field

from .product_get_import_products_info_response_result import ProductGetImportProductsInfoResponseResult


class ProductGetImportProductsInfoResponse(BaseModel):
    """
    object model
    """

    result: Optional[ProductGetImportProductsInfoResponseResult] = Field(alias="result", default=None)
