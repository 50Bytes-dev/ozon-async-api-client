from typing import *

from pydantic import BaseModel, Field

from .v1status_code_name_pair import V1statusCodeNamePair


class V1productCertificateProductStatusListResponse(BaseModel):
    """
    object model
    """

    result: Optional[List[Optional[V1statusCodeNamePair]]] = Field(alias="result", default=None)
