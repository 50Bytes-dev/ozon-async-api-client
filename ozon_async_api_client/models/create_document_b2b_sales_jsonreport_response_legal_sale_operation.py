from typing import *

from pydantic import BaseModel, Field

from .create_document_b2b_sales_jsonreport_response_legal_sale_operation_type import \
    CreateDocumentB2bSalesJSONReportResponseLegalSaleOperationType


class CreateDocumentB2bSalesJSONReportResponseLegalSaleOperation(BaseModel):
    """
    None model
    """

    amount: Optional[float] = Field(alias="amount", default=None)

    cost_without_vat: Optional[float] = Field(alias="cost_without_vat", default=None)

    date: Optional[str] = Field(alias="date", default=None)

    gtd_number: Optional[str] = Field(alias="gtd_number", default=None)

    origin_country: Optional[str] = Field(alias="origin_country", default=None)

    posting_number: Optional[str] = Field(alias="posting_number", default=None)

    price: Optional[float] = Field(alias="price", default=None)

    quantity: Optional[int] = Field(alias="quantity", default=None)

    rnpt_number: Optional[str] = Field(alias="rnpt_number", default=None)

    type: Optional[CreateDocumentB2bSalesJSONReportResponseLegalSaleOperationType] = Field(alias="type", default=None)

    vat_amount: Optional[float] = Field(alias="vat_amount", default=None)

    vat_rate: Optional[float] = Field(alias="vat_rate", default=None)
