from typing import *

from pydantic import BaseModel, Field


class FbsPostingFbsPostingAnalyticsData(BaseModel):
    """
    object model

    Аналитические данные.
    """

    city: Optional[str] = Field(alias="city", default=None)

    delivery_type: Optional[str] = Field(alias="delivery_type", default=None)

    is_legal: Optional[bool] = Field(alias="is_legal", default=None)

    is_premium: Optional[bool] = Field(alias="is_premium", default=None)

    payment_type_group_name: Optional[str] = Field(alias="payment_type_group_name", default=None)

    region: Optional[str] = Field(alias="region", default=None)
