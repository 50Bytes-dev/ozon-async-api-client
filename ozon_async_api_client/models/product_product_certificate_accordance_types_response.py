from typing import *

from pydantic import BaseModel, Field

from .product_product_certificate_accordance_types_response_type import \
    ProductProductCertificateAccordanceTypesResponseType


class ProductProductCertificateAccordanceTypesResponse(BaseModel):
    """
    object model
    """

    result: Optional[List[Optional[ProductProductCertificateAccordanceTypesResponseType]]] = Field(
        alias="result", default=None
    )
