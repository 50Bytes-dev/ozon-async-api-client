from typing import *

from pydantic import BaseModel, Field


class V1certificate(BaseModel):
    """
    object model

    Информация о сертификате.
    """

    certificate_id: Optional[int] = Field(alias="certificate_id", default=None)

    certificate_number: Optional[str] = Field(alias="certificate_number", default=None)

    certificate_name: Optional[str] = Field(alias="certificate_name", default=None)

    type_code: Optional[str] = Field(alias="type_code", default=None)

    status_code: Optional[str] = Field(alias="status_code", default=None)

    accordance_type_code: Optional[str] = Field(alias="accordance_type_code", default=None)

    rejection_reason_code: Optional[str] = Field(alias="rejection_reason_code", default=None)

    verification_comment: Optional[str] = Field(alias="verification_comment", default=None)

    issue_date: Optional[str] = Field(alias="issue_date", default=None)

    expire_date: Optional[str] = Field(alias="expire_date", default=None)

    products_count: Optional[int] = Field(alias="products_count", default=None)
