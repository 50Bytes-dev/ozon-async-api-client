from typing import *

from pydantic import BaseModel, Field


class V1productCertificateProductsListRequest(BaseModel):
    """
    object model
    """

    certificate_id: int = Field(alias="certificate_id")

    product_status_code: Optional[str] = Field(alias="product_status_code", default=None)

    page: int = Field(alias="page")

    page_size: int = Field(alias="page_size")
