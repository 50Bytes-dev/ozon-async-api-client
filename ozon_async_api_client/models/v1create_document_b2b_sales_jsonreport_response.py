from typing import *

from pydantic import BaseModel, Field

from .create_document_b2b_sales_jsonreport_response_legal_sale_invoice import \
    CreateDocumentB2bSalesJSONReportResponseLegalSaleInvoice
from .create_document_b2b_sales_jsonreport_response_seller_info import \
    CreateDocumentB2bSalesJSONReportResponseSellerInfo


class V1createDocumentB2bSalesJSONReportResponse(BaseModel):
    """
    None model
    """

    date_from: Optional[str] = Field(alias="date_from", default=None)

    date_to: Optional[str] = Field(alias="date_to", default=None)

    invoices: Optional[List[Optional[CreateDocumentB2bSalesJSONReportResponseLegalSaleInvoice]]] = Field(
        alias="invoices", default=None
    )

    seller_info: Optional[CreateDocumentB2bSalesJSONReportResponseSellerInfo] = Field(alias="seller_info", default=None)
