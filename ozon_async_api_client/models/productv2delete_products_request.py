from typing import *

from pydantic import BaseModel, Field

from .delete_products_request_product import DeleteProductsRequestProduct


class Productv2deleteProductsRequest(BaseModel):
    """
    object model
    """

    products: List[DeleteProductsRequestProduct] = Field(alias="products")
