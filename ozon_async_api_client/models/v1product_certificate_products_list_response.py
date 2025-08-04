from typing import *

from pydantic import BaseModel, Field

from .v1product_certificate_products_list_response_result import V1productCertificateProductsListResponseResult


class V1productCertificateProductsListResponse(BaseModel):
    """
    object model
    """

    result: Optional[V1productCertificateProductsListResponseResult] = Field(alias="result", default=None)
