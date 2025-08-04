from typing import *

from pydantic import BaseModel, Field

from .product_certification_list_response_certificationv2 import ProductCertificationListResponseCertificationv2


class V2productCertificationListResponse(BaseModel):
    """
    None model
    """

    certification: Optional[List[Optional[ProductCertificationListResponseCertificationv2]]] = Field(
        alias="certification", default=None
    )

    total: Optional[int] = Field(alias="total", default=None)
