from typing import *

from pydantic import BaseModel, Field


class ProductCertificateProductsListResponseProduct(BaseModel):
    """
    object model
    """

    product_id: Optional[int] = Field(alias="product_id", default=None)

    product_status_code: Optional[str] = Field(alias="product_status_code", default=None)
