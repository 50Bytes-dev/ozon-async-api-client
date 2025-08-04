from typing import *

from pydantic import BaseModel, Field


class V1productCertificateDeleteRequest(BaseModel):
    """
    object model
    """

    certificate_id: int = Field(alias="certificate_id")
