from typing import *

from pydantic import BaseModel, Field

from .v2product_certificate_accordance_types_response_type import V2productCertificateAccordanceTypesResponseType


class V2productCertificateAccordanceTypesResponseResult(BaseModel):
    """
    object model

    Список типов соответствия требованиям.
    """

    base: Optional[List[Optional[V2productCertificateAccordanceTypesResponseType]]] = Field(alias="base", default=None)

    hazard: Optional[List[Optional[V2productCertificateAccordanceTypesResponseType]]] = Field(
        alias="hazard", default=None
    )
