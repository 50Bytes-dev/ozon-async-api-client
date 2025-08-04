from typing import *

from pydantic import BaseModel, Field

from .v1status_code_name_pair_rejection import V1statusCodeNamePairRejection


class V1productCertificateRejectionReasonsListResponse(BaseModel):
    """
    object model
    """

    result: Optional[List[Optional[V1statusCodeNamePairRejection]]] = Field(alias="result", default=None)
