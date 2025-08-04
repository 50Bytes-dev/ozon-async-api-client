from typing import *

from pydantic import BaseModel, Field


class ProductProductCertificateBindRequest(BaseModel):
    """
    object model
    """

    certificate_id: Optional[int] = Field(alias="certificate_id", default=None)

    product_id: Optional[List[int]] = Field(alias="product_id", default=None)
