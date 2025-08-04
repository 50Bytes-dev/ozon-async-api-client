from typing import *

from pydantic import BaseModel, Field

from .product_certificate_unbind_response_item import ProductCertificateUnbindResponseItem


class V1productCertificateUnbindResponse(BaseModel):
    """
    object model
    """

    result: Optional[List[Optional[ProductCertificateUnbindResponseItem]]] = Field(alias="result", default=None)
