from typing import *

from pydantic import BaseModel, Field

from .posting_additional_data_item import PostingAdditionalDataItem
from .posting_legal_info import PostingLegalInfo
from .posting_posting_analytics_data import PostingPostingAnalyticsData
from .posting_posting_financial_data import PostingPostingFinancialData
from .posting_posting_product import PostingPostingProduct


class ListPostingCodesResponsePosting(BaseModel):
    """
    None model
    """

    additional_data: Optional[List[Optional[PostingAdditionalDataItem]]] = Field(alias="additional_data", default=None)

    analytics_data: Optional[PostingPostingAnalyticsData] = Field(alias="analytics_data", default=None)

    cancel_reason_id: Optional[int] = Field(alias="cancel_reason_id", default=None)

    created_at: Optional[str] = Field(alias="created_at", default=None)

    financial_data: Optional[PostingPostingFinancialData] = Field(alias="financial_data", default=None)

    in_process_at: Optional[str] = Field(alias="in_process_at", default=None)

    legal_info: Optional[PostingLegalInfo] = Field(alias="legal_info", default=None)

    order_id: Optional[int] = Field(alias="order_id", default=None)

    order_number: Optional[str] = Field(alias="order_number", default=None)

    posting_number: Optional[str] = Field(alias="posting_number", default=None)

    products: Optional[List[Optional[PostingPostingProduct]]] = Field(alias="products", default=None)

    status: Optional[str] = Field(alias="status", default=None)

    waiting_deadline_for_digital_code: Optional[str] = Field(alias="waiting_deadline_for_digital_code", default=None)
