from typing import *

from pydantic import BaseModel, Field

from .fbo_posting_fbo_posting_analytics_data import FboPostingFboPostingAnalyticsData
from .v2additional_data_item import V2additionalDataItem
from .v2fbo_single_posting_legal_info import V2fboSinglePostingLegalInfo
from .v2posting_financial_data import V2postingFinancialData
from .v2posting_product import V2postingProduct


class V2fboPosting(BaseModel):
    """
    object model

    Результат запроса.
    """

    additional_data: Optional[List[Optional[V2additionalDataItem]]] = Field(alias="additional_data", default=None)

    analytics_data: Optional[FboPostingFboPostingAnalyticsData] = Field(alias="analytics_data", default=None)

    cancel_reason_id: Optional[int] = Field(alias="cancel_reason_id", default=None)

    created_at: Optional[str] = Field(alias="created_at", default=None)

    financial_data: Optional[V2postingFinancialData] = Field(alias="financial_data", default=None)

    in_process_at: Optional[str] = Field(alias="in_process_at", default=None)

    legal_info: Optional[V2fboSinglePostingLegalInfo] = Field(alias="legal_info", default=None)

    order_id: Optional[int] = Field(alias="order_id", default=None)

    order_number: Optional[str] = Field(alias="order_number", default=None)

    posting_number: Optional[str] = Field(alias="posting_number", default=None)

    products: Optional[List[Optional[V2postingProduct]]] = Field(alias="products", default=None)

    status: Optional[str] = Field(alias="status", default=None)
