from typing import *

from pydantic import BaseModel, Field


class V2productCertificateAccordanceTypesResponseType(BaseModel):
    """
    object model
    """

    code: Optional[str] = Field(alias="code", default=None)

    title: Optional[str] = Field(alias="title", default=None)
