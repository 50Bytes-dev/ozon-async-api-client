from typing import *

from pydantic import BaseModel, Field

from .fbs_posting_detail_courier import FbsPostingDetailCourier
from .fbs_posting_detail_prr_option import FbsPostingDetailPrrOption
from .v2fbo_single_posting_legal_info import V2fboSinglePostingLegalInfo
from .v3additional_data_item import V3additionalDataItem
from .v3addressee import V3addressee
from .v3barcodes import V3barcodes
from .v3cancellation import V3cancellation
from .v3customer import V3customer
from .v3delivery_method import V3deliveryMethod
from .v3fbs_posting_analytics_data import V3fbsPostingAnalyticsData
from .v3fbs_posting_detail_optional import V3fbsPostingDetailOptional
from .v3fbs_posting_detail_related_postings import V3fbsPostingDetailRelatedPostings
from .v3fbs_posting_product_exemplars_v3 import V3fbsPostingProductExemplarsV3
from .v3fbs_posting_requirements_v3 import V3fbsPostingRequirementsV3
from .v3fbs_tariffication import V3fbsTariffication
from .v3posting_financial_data import V3postingFinancialData
from .v3posting_product_detail import V3postingProductDetail


class V3fbsPostingDetail(BaseModel):
    """
    object model

    Информация об отправлении.
    """

    additional_data: Optional[List[Optional[V3additionalDataItem]]] = Field(alias="additional_data", default=None)

    addressee: Optional[V3addressee] = Field(alias="addressee", default=None)

    analytics_data: Optional[V3fbsPostingAnalyticsData] = Field(alias="analytics_data", default=None)

    available_actions: Optional[Any] = Field(alias="available_actions", default=None)

    barcodes: Optional[V3barcodes] = Field(alias="barcodes", default=None)

    cancellation: Optional[V3cancellation] = Field(alias="cancellation", default=None)

    courier: Optional[FbsPostingDetailCourier] = Field(alias="courier", default=None)

    customer: Optional[V3customer] = Field(alias="customer", default=None)

    delivering_date: Optional[str] = Field(alias="delivering_date", default=None)

    delivery_method: Optional[V3deliveryMethod] = Field(alias="delivery_method", default=None)

    delivery_price: Optional[str] = Field(alias="delivery_price", default=None)

    financial_data: Optional[V3postingFinancialData] = Field(alias="financial_data", default=None)

    in_process_at: Optional[str] = Field(alias="in_process_at", default=None)

    is_express: Optional[bool] = Field(alias="is_express", default=None)

    is_multibox: Optional[bool] = Field(alias="is_multibox", default=None)

    legal_info: Optional[V2fboSinglePostingLegalInfo] = Field(alias="legal_info", default=None)

    multi_box_qty: Optional[int] = Field(alias="multi_box_qty", default=None)

    optional: Optional[V3fbsPostingDetailOptional] = Field(alias="optional", default=None)

    order_id: Optional[int] = Field(alias="order_id", default=None)

    order_number: Optional[str] = Field(alias="order_number", default=None)

    parent_posting_number: Optional[str] = Field(alias="parent_posting_number", default=None)

    pickup_code_verified_at: Optional[str] = Field(alias="pickup_code_verified_at", default=None)

    posting_number: Optional[str] = Field(alias="posting_number", default=None)

    product_exemplars: Optional[V3fbsPostingProductExemplarsV3] = Field(alias="product_exemplars", default=None)

    products: Optional[List[Optional[V3postingProductDetail]]] = Field(alias="products", default=None)

    provider_status: Optional[str] = Field(alias="provider_status", default=None)

    prr_option: Optional[FbsPostingDetailPrrOption] = Field(alias="prr_option", default=None)

    related_postings: Optional[V3fbsPostingDetailRelatedPostings] = Field(alias="related_postings", default=None)

    requirements: Optional[V3fbsPostingRequirementsV3] = Field(alias="requirements", default=None)

    shipment_date: Optional[str] = Field(alias="shipment_date", default=None)

    status: Optional[str] = Field(alias="status", default=None)

    substatus: Optional[str] = Field(alias="substatus", default=None)

    previous_substatus: Optional[str] = Field(alias="previous_substatus", default=None)

    tpl_integration_type: Optional[str] = Field(alias="tpl_integration_type", default=None)

    tracking_number: Optional[str] = Field(alias="tracking_number", default=None)

    tariffication: Optional[List[Optional[V3fbsTariffication]]] = Field(alias="tariffication", default=None)
