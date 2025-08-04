from typing import *

from pydantic import BaseModel, Field


class PostingPostingAnalyticsData(BaseModel):
    """
    None model

    Данные аналитики.
    """

    city: Optional[str] = Field(alias="city", default=None)

    delivery_type: Optional[str] = Field(alias="delivery_type", default=None)

    is_legal: Optional[bool] = Field(alias="is_legal", default=None)

    is_premium: Optional[bool] = Field(alias="is_premium", default=None)

    payment_type_group_name: Optional[str] = Field(alias="payment_type_group_name", default=None)

    region: Optional[str] = Field(alias="region", default=None)

    warehouse_id: Optional[int] = Field(alias="warehouse_id", default=None)

    warehouse_name: Optional[str] = Field(alias="warehouse_name", default=None)
