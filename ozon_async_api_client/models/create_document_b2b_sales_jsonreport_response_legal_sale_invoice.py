from typing import *

from pydantic import BaseModel, Field

from .create_document_b2b_sales_jsonreport_response_buyer import CreateDocumentB2bSalesJSONReportResponseBuyer
from .create_document_b2b_sales_jsonreport_response_invoice_info import \
    CreateDocumentB2bSalesJSONReportResponseInvoiceInfo
from .create_document_b2b_sales_jsonreport_response_legal_sale_operation import \
    CreateDocumentB2bSalesJSONReportResponseLegalSaleOperation


class CreateDocumentB2bSalesJSONReportResponseLegalSaleInvoice(BaseModel):
    """
    None model
    """

    buyer_info: Optional[CreateDocumentB2bSalesJSONReportResponseBuyer] = Field(alias="buyer_info", default=None)

    currency: Optional[str] = Field(alias="currency", default=None)

    currency_code: Optional[int] = Field(alias="currency_code", default=None)

    info: Optional[CreateDocumentB2bSalesJSONReportResponseInvoiceInfo] = Field(alias="info", default=None)

    offer_id: Optional[str] = Field(alias="offer_id", default=None)

    operations: Optional[List[Optional[CreateDocumentB2bSalesJSONReportResponseLegalSaleOperation]]] = Field(
        alias="operations", default=None
    )

    product_name: Optional[str] = Field(alias="product_name", default=None)

    sku: Optional[int] = Field(alias="sku", default=None)

    unit_code: Optional[int] = Field(alias="unit_code", default=None)

    unit_name: Optional[str] = Field(alias="unit_name", default=None)
