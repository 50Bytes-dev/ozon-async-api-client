from typing import *

from pydantic import BaseModel, Field

from .get_returns_list_response_additional_info import GetReturnsListResponseAdditionalInfo
from .get_returns_list_response_exemplar import GetReturnsListResponseExemplar
from .get_returns_list_response_logistic import GetReturnsListResponseLogistic
from .get_returns_list_response_place_now import GetReturnsListResponsePlaceNow
from .get_returns_list_response_place_target import GetReturnsListResponsePlaceTarget
from .get_returns_list_response_product import GetReturnsListResponseProduct
from .get_returns_list_response_storage import GetReturnsListResponseStorage
from .get_returns_list_response_visual import GetReturnsListResponseVisual


class GetReturnsListResponseReturnsItem(BaseModel):
    """
    object model
    """

    exemplars: Optional[List[Optional[GetReturnsListResponseExemplar]]] = Field(alias="exemplars", default=None)

    id: Optional[int] = Field(alias="id", default=None)

    company_id: Optional[int] = Field(alias="company_id", default=None)

    return_reason_name: Optional[str] = Field(alias="return_reason_name", default=None)

    type: Optional[str] = Field(alias="type", default=None)

    schema: Optional[str] = Field(alias="schema", default=None)

    order_id: Optional[int] = Field(alias="order_id", default=None)

    order_number: Optional[str] = Field(alias="order_number", default=None)

    place: Optional[GetReturnsListResponsePlaceNow] = Field(alias="place", default=None)

    target_place: Optional[GetReturnsListResponsePlaceTarget] = Field(alias="target_place", default=None)

    storage: Optional[GetReturnsListResponseStorage] = Field(alias="storage", default=None)

    product: Optional[GetReturnsListResponseProduct] = Field(alias="product", default=None)

    logistic: Optional[GetReturnsListResponseLogistic] = Field(alias="logistic", default=None)

    visual: Optional[GetReturnsListResponseVisual] = Field(alias="visual", default=None)

    additional_info: Optional[GetReturnsListResponseAdditionalInfo] = Field(alias="additional_info", default=None)

    source_id: Optional[int] = Field(alias="source_id", default=None)

    posting_number: Optional[str] = Field(alias="posting_number", default=None)

    clearing_id: Optional[int] = Field(alias="clearing_id", default=None)

    return_clearing_id: Optional[int] = Field(alias="return_clearing_id", default=None)
