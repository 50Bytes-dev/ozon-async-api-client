from typing import *

from pydantic import BaseModel, Field

from .product_product_certificate_types_response_type import ProductProductCertificateTypesResponseType


class ProductProductCertificateTypesResponse(BaseModel):
    """
    object model
    """

    result: Optional[List[Optional[ProductProductCertificateTypesResponseType]]] = Field(alias="result", default=None)
