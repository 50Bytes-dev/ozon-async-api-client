from typing import *

from pydantic import BaseModel, Field

from .v2product import V2product
from .v2returns_rfbs_list_v2response_state import V2returnsRfbsListV2responseState


class ReturnsRfbsListResponseReturns(BaseModel):
    """
    object model

    Данные о заявках.
    """

    client_name: Optional[str] = Field(alias="client_name", default=None)

    created_at: Optional[str] = Field(alias="created_at", default=None)

    order_number: Optional[str] = Field(alias="order_number", default=None)

    posting_number: Optional[str] = Field(alias="posting_number", default=None)

    product: Optional[V2product] = Field(alias="product", default=None)

    return_id: Optional[int] = Field(alias="return_id", default=None)

    return_number: Optional[str] = Field(alias="return_number", default=None)

    state: Optional[V2returnsRfbsListV2responseState] = Field(alias="state", default=None)
