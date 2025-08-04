from typing import *

from pydantic import BaseModel, Field

from .invoice_get_v2response_result import InvoiceGetV2responseResult


class V2invoiceGetV2response(BaseModel):
    """
    object model
    """

    result: Optional[InvoiceGetV2responseResult] = Field(alias="result", default=None)
