from typing import *

from pydantic import BaseModel, Field

from .v1product_certificate_list_response_result import V1productCertificateListResponseResult


class V1productCertificateListResponse(BaseModel):
    """
    object model
    """

    result: Optional[V1productCertificateListResponseResult] = Field(alias="result", default=None)
