from typing import *

from pydantic import BaseModel, Field


class V1productCertificateUnbindRequest(BaseModel):
    """
    object model
    """

    certificate_id: int = Field(alias="certificate_id")

    product_id: List[str] = Field(alias="product_id")
