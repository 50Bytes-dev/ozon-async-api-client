from typing import *

from pydantic import BaseModel, Field


class BrandCompanyCertificationListResponseBrandCertification(BaseModel):
    """
    object model
    """

    brand_name: Optional[str] = Field(alias="brand_name", default=None)

    has_certificate: Optional[bool] = Field(alias="has_certificate", default=None)
