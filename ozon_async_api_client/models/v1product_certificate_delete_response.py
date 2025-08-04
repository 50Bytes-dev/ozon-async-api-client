from typing import *

from pydantic import BaseModel, Field

from .v1product_certificate_delete_response_result import V1productCertificateDeleteResponseResult


class V1productCertificateDeleteResponse(BaseModel):
    """
    object model
    """

    result: Optional[V1productCertificateDeleteResponseResult] = Field(alias="result", default=None)
