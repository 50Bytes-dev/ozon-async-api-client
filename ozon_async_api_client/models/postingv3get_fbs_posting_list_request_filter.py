from typing import *

from pydantic import BaseModel, Field

from .postinglist_v3status import PostinglistV3status


class Postingv3getFbsPostingListRequestFilter(BaseModel):
    """
    object model

    Фильтр.
    """

    delivery_method_id: Optional[List[int]] = Field(alias="delivery_method_id", default=None)

    is_quantum: Optional[bool] = Field(alias="is_quantum", default=None)

    order_id: Optional[int] = Field(alias="order_id", default=None)

    provider_id: Optional[List[int]] = Field(alias="provider_id", default=None)

    since: str = Field(alias="since")

    to: str = Field(alias="to")

    status: Optional[str] = Field(alias="status", default=None)

    warehouse_id: Optional[List[str]] = Field(alias="warehouse_id", default=None)

    last_changed_status_date: Optional[PostinglistV3status] = Field(alias="last_changed_status_date", default=None)
