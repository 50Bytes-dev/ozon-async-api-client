from typing import *

from pydantic import BaseModel, Field

from .brand_company_certification_list_response_brand_certification_result import \
    BrandCompanyCertificationListResponseBrandCertificationResult


class BrandBrandCompanyCertificationListResponse(BaseModel):
    """
    object model
    """

    result: Optional[BrandCompanyCertificationListResponseBrandCertificationResult] = Field(
        alias="result", default=None
    )
