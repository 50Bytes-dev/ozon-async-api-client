from typing import *

from pydantic import BaseModel, Field

from .v2product_certificate_accordance_types_response_result import V2productCertificateAccordanceTypesResponseResult


class V2productCertificateAccordanceTypesResponse(BaseModel):
    """
    object model
    """

    result: Optional[V2productCertificateAccordanceTypesResponseResult] = Field(alias="result", default=None)
