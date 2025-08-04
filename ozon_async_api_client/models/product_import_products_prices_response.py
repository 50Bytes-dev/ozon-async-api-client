from typing import *

from pydantic import BaseModel, Field

from .product_import_products_prices_response_process_result import ProductImportProductsPricesResponseProcessResult


class ProductImportProductsPricesResponse(BaseModel):
    """
    object model
    """

    result: Optional[List[Optional[ProductImportProductsPricesResponseProcessResult]]] = Field(
        alias="result", default=None
    )
