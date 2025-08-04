from typing import *

from pydantic import BaseModel, Field

from .product_certification_list_response_certification import ProductCertificationListResponseCertification


class ProductCertificationListResponseCertificationResult(BaseModel):
    """
    object model

    Результат запроса.
    """

    certification: Optional[List[Optional[ProductCertificationListResponseCertification]]] = Field(
        alias="certification", default=None
    )

    total: Optional[int] = Field(alias="total", default=None)
