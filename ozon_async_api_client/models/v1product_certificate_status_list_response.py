from typing import *

from pydantic import BaseModel, Field

from .v1status_code_name_pair_statuses import V1statusCodeNamePairStatuses


class V1productCertificateStatusListResponse(BaseModel):
    """
    object model
    """

    result: Optional[List[Optional[V1statusCodeNamePairStatuses]]] = Field(alias="result", default=None)
