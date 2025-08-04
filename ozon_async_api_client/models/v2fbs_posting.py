from typing import *

from pydantic import BaseModel, Field

from .fbs_posting_barcodes import FbsPostingBarcodes
from .fbs_posting_fbs_posting_analytics_data import FbsPostingFbsPostingAnalyticsData
from .v2fbs_posting_product import V2fbsPostingProduct
from .v2posting_financial_data import V2postingFinancialData


class V2fbsPosting(BaseModel):
    """
    object model

    Результаты запроса.
    """

    analytics_data: Optional[FbsPostingFbsPostingAnalyticsData] = Field(alias="analytics_data", default=None)

    barcodes: Optional[FbsPostingBarcodes] = Field(alias="barcodes", default=None)

    cancel_reason_id: Optional[int] = Field(alias="cancel_reason_id", default=None)

    created_at: Optional[str] = Field(alias="created_at", default=None)

    financial_data: Optional[V2postingFinancialData] = Field(alias="financial_data", default=None)

    in_process_at: Optional[str] = Field(alias="in_process_at", default=None)

    order_id: Optional[int] = Field(alias="order_id", default=None)

    order_number: Optional[str] = Field(alias="order_number", default=None)

    posting_number: Optional[str] = Field(alias="posting_number", default=None)

    products: Optional[List[Optional[V2fbsPostingProduct]]] = Field(alias="products", default=None)

    shipment_date: Optional[str] = Field(alias="shipment_date", default=None)

    status: Optional[str] = Field(alias="status", default=None)
