from typing import *

from pydantic import BaseModel, Field

from .product_get_product_info_description_response_product import ProductGetProductInfoDescriptionResponseProduct


class ProductGetProductInfoDescriptionResponse(BaseModel):
    """
    object model
    """

    result: Optional[ProductGetProductInfoDescriptionResponseProduct] = Field(alias="result", default=None)
