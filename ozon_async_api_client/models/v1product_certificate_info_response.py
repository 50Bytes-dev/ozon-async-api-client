from typing import *

from pydantic import BaseModel, Field

from .v1certificate import V1certificate


class V1productCertificateInfoResponse(BaseModel):
    """
    object model
    """

    result: Optional[V1certificate] = Field(alias="result", default=None)
