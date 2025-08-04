from typing import *

from pydantic import BaseModel, Field

from .returns_rfbs_get_v2response_available_action import ReturnsRfbsGetV2responseAvailableAction
from .returns_rfbs_get_v2response_client_return_method_type import ReturnsRfbsGetV2responseClientReturnMethodType
from .returns_rfbs_get_v2response_rejection_reason import ReturnsRfbsGetV2responseRejectionReason
from .returns_rfbs_get_v2response_return_reason import ReturnsRfbsGetV2responseReturnReason
from .v2product import V2product
from .v2returns_rfbs_get_v2response_state import V2returnsRfbsGetV2responseState


class ReturnsRfbsGetResponseReturns(BaseModel):
    """
    object model

    Данные о заявке.
    """

    available_actions: Optional[List[Optional[ReturnsRfbsGetV2responseAvailableAction]]] = Field(
        alias="available_actions", default=None
    )

    client_name: Optional[str] = Field(alias="client_name", default=None)

    client_photo: Optional[List[str]] = Field(alias="client_photo", default=None)

    client_return_method_type: Optional[ReturnsRfbsGetV2responseClientReturnMethodType] = Field(
        alias="client_return_method_type", default=None
    )

    comment: Optional[str] = Field(alias="comment", default=None)

    created_at: Optional[str] = Field(alias="created_at", default=None)

    order_number: Optional[str] = Field(alias="order_number", default=None)

    posting_number: Optional[str] = Field(alias="posting_number", default=None)

    product: Optional[V2product] = Field(alias="product", default=None)

    rejection_comment: Optional[str] = Field(alias="rejection_comment", default=None)

    rejection_reason: Optional[List[Optional[ReturnsRfbsGetV2responseRejectionReason]]] = Field(
        alias="rejection_reason", default=None
    )

    return_method_description: Optional[str] = Field(alias="return_method_description", default=None)

    return_number: Optional[str] = Field(alias="return_number", default=None)

    return_reason: Optional[ReturnsRfbsGetV2responseReturnReason] = Field(alias="return_reason", default=None)

    ru_post_tracking_number: Optional[str] = Field(alias="ru_post_tracking_number", default=None)

    state: Optional[V2returnsRfbsGetV2responseState] = Field(alias="state", default=None)

    warehouse_id: Optional[int] = Field(alias="warehouse_id", default=None)
