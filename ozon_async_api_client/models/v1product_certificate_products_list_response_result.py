from typing import *

from pydantic import BaseModel, Field

from .product_certificate_products_list_response_product import ProductCertificateProductsListResponseProduct


class V1productCertificateProductsListResponseResult(BaseModel):
    """
    object model

    Товары, привязанные к сертификату.
    """

    items: Optional[List[Optional[ProductCertificateProductsListResponseProduct]]] = Field(alias="items", default=None)

    count: Optional[int] = Field(alias="count", default=None)
