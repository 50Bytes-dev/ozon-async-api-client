from typing import *

from pydantic import BaseModel, Field

from .get_product_info_list_response_commission import GetProductInfoListResponseCommission
from .get_product_info_list_response_error import GetProductInfoListResponseError
from .get_product_info_list_response_model_info import GetProductInfoListResponseModelInfo
from .get_product_info_list_response_price_indexes import GetProductInfoListResponsePriceIndexes
from .get_product_info_list_response_source import GetProductInfoListResponseSource
from .get_product_info_list_response_statuses import GetProductInfoListResponseStatuses
from .get_product_info_list_response_stocks import GetProductInfoListResponseStocks
from .get_product_info_list_response_visibility_details import GetProductInfoListResponseVisibilityDetails


class V3getProductInfoListResponseItem(BaseModel):
    """
    object model
    """

    barcodes: Optional[List[str]] = Field(alias="barcodes", default=None)

    color_image: Optional[List[str]] = Field(alias="color_image", default=None)

    commissions: Optional[List[Optional[GetProductInfoListResponseCommission]]] = Field(
        alias="commissions", default=None
    )

    created_at: Optional[str] = Field(alias="created_at", default=None)

    currency_code: Optional[str] = Field(alias="currency_code", default=None)

    description_category_id: Optional[int] = Field(alias="description_category_id", default=None)

    discounted_fbo_stocks: Optional[int] = Field(alias="discounted_fbo_stocks", default=None)

    errors: Optional[List[Optional[GetProductInfoListResponseError]]] = Field(alias="errors", default=None)

    has_discounted_fbo_item: Optional[bool] = Field(alias="has_discounted_fbo_item", default=None)

    id: Optional[int] = Field(alias="id", default=None)

    images: Optional[List[str]] = Field(alias="images", default=None)

    images360: Optional[List[str]] = Field(alias="images360", default=None)

    is_archived: Optional[bool] = Field(alias="is_archived", default=None)

    is_autoarchived: Optional[bool] = Field(alias="is_autoarchived", default=None)

    is_discounted: Optional[bool] = Field(alias="is_discounted", default=None)

    is_kgt: Optional[bool] = Field(alias="is_kgt", default=None)

    is_prepayment_allowed: Optional[bool] = Field(alias="is_prepayment_allowed", default=None)

    is_super: Optional[bool] = Field(alias="is_super", default=None)

    marketing_price: Optional[str] = Field(alias="marketing_price", default=None)

    min_price: Optional[str] = Field(alias="min_price", default=None)

    model_info: Optional[GetProductInfoListResponseModelInfo] = Field(alias="model_info", default=None)

    name: Optional[str] = Field(alias="name", default=None)

    offer_id: Optional[str] = Field(alias="offer_id", default=None)

    old_price: Optional[str] = Field(alias="old_price", default=None)

    price: Optional[str] = Field(alias="price", default=None)

    price_indexes: Optional[GetProductInfoListResponsePriceIndexes] = Field(alias="price_indexes", default=None)

    primary_image: Optional[List[str]] = Field(alias="primary_image", default=None)

    sources: Optional[List[Optional[GetProductInfoListResponseSource]]] = Field(alias="sources", default=None)

    statuses: Optional[GetProductInfoListResponseStatuses] = Field(alias="statuses", default=None)

    stocks: Optional[GetProductInfoListResponseStocks] = Field(alias="stocks", default=None)

    type_id: Optional[int] = Field(alias="type_id", default=None)

    updated_at: Optional[str] = Field(alias="updated_at", default=None)

    vat: Optional[str] = Field(alias="vat", default=None)

    visibility_details: Optional[GetProductInfoListResponseVisibilityDetails] = Field(
        alias="visibility_details", default=None
    )

    volume_weight: Optional[float] = Field(alias="volume_weight", default=None)
