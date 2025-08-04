from typing import *

from pydantic import BaseModel, Field


class V1productCertificateInfoRequest(BaseModel):
    """
    object model
    """

    certificate_number: str = Field(alias="certificate_number")
