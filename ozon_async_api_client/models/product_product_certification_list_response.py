from typing import *

from pydantic import BaseModel, Field

from .product_certification_list_response_certification_result import \
    ProductCertificationListResponseCertificationResult


class ProductProductCertificationListResponse(BaseModel):
    """
    object model
    """

    result: Optional[ProductCertificationListResponseCertificationResult] = Field(alias="result", default=None)
