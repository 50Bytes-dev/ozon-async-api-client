from typing import *

from pydantic import BaseModel, Field


class ProductProductCertificateAccordanceTypesResponseType(BaseModel):
    """
    object model
    """

    name: Optional[str] = Field(alias="name", default=None)

    value: Optional[str] = Field(alias="value", default=None)
