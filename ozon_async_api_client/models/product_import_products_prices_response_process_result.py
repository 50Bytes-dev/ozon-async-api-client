from typing import *

from pydantic import BaseModel, Field

from .product_import_products_prices_response_error import ProductImportProductsPricesResponseError


class ProductImportProductsPricesResponseProcessResult(BaseModel):
    """
    object model
    """

    errors: Optional[List[Optional[ProductImportProductsPricesResponseError]]] = Field(alias="errors", default=None)

    offer_id: Optional[str] = Field(alias="offer_id", default=None)

    product_id: Optional[int] = Field(alias="product_id", default=None)

    updated: Optional[bool] = Field(alias="updated", default=None)
