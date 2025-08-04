from typing import *

from pydantic import BaseModel, Field

from .common_language import CommonLanguage


class V1createDocumentB2bSalesReportRequest(BaseModel):
    """
    None model
    """

    date: Optional[str] = Field(alias="date", default=None)

    language: Optional[CommonLanguage] = Field(alias="language", default=None)
