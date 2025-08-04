from typing import *

from pydantic import BaseModel, Field


class V1productActionTimerStatusResponseStatuses(BaseModel):
    """
    None model
    """

    expired_at: Optional[str] = Field(alias="expired_at", default=None)

    min_price_for_auto_actions_enabled: Optional[bool] = Field(alias="min_price_for_auto_actions_enabled", default=None)

    product_id: Optional[int] = Field(alias="product_id", default=None)
