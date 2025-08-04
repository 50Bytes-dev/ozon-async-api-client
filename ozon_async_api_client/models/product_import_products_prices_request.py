from typing import *

from pydantic import BaseModel, Field

from .product_import_products_prices_request_price import ProductImportProductsPricesRequestPrice


class ProductImportProductsPricesRequest(BaseModel):
    """
    object model
    """

    prices: Optional[List[Optional[ProductImportProductsPricesRequestPrice]]] = Field(alias="prices", default=None)
