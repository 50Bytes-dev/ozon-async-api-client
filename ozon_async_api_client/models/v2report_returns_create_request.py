from typing import *

from pydantic import BaseModel, Field

from .report_language import ReportLanguage


class V2reportReturnsCreateRequest(BaseModel):
    """
    object model
    """

    filter: Optional[Dict[str, Any]] = Field(alias="filter", default=None)

    language: Optional[ReportLanguage] = Field(alias="language", default=None)
