from typing import *

from pydantic import BaseModel, Field

from .report_create_company_products_report_request_visibility import ReportCreateCompanyProductsReportRequestVisibility
from .report_language import ReportLanguage


class ReportCreateCompanyProductsReportRequest(BaseModel):
    """
    CreateCompanyProductsReport model
    """

    language: Optional[ReportLanguage] = Field(alias="language", default=None)

    offer_id: Optional[List[str]] = Field(alias="offer_id", default=None)

    search: Optional[str] = Field(alias="search", default=None)

    sku: Optional[List[int]] = Field(alias="sku", default=None)

    visibility: Optional[ReportCreateCompanyProductsReportRequestVisibility] = Field(alias="visibility", default=None)
