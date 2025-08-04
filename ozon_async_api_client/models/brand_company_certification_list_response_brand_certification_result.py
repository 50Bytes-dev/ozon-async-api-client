from typing import *

from pydantic import BaseModel, Field

from .brand_company_certification_list_response_brand_certification import \
    BrandCompanyCertificationListResponseBrandCertification


class BrandCompanyCertificationListResponseBrandCertificationResult(BaseModel):
    """
    object model

    Результат запроса.
    """

    brand_certification: Optional[List[Optional[BrandCompanyCertificationListResponseBrandCertification]]] = Field(
        alias="brand_certification", default=None
    )

    total: Optional[int] = Field(alias="total", default=None)
