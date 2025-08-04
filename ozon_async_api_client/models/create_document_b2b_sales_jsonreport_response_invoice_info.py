from typing import *

from pydantic import BaseModel, Field

from .create_document_b2b_sales_jsonreport_response_invoice_info_type import \
    CreateDocumentB2bSalesJSONReportResponseInvoiceInfoType


class CreateDocumentB2bSalesJSONReportResponseInvoiceInfo(BaseModel):
    """
    None model

    Информация о счёте-фактуре.
    """

    date: Optional[str] = Field(alias="date", default=None)

    number: Optional[str] = Field(alias="number", default=None)

    status: Optional[str] = Field(alias="status", default=None)

    type: Optional[CreateDocumentB2bSalesJSONReportResponseInvoiceInfoType] = Field(alias="type", default=None)
