from typing import *

from pydantic import BaseModel, Field


class V3fbsPostingAnalyticsData(BaseModel):
    """
    object model

    Данные аналитики.
    """

    city: Optional[str] = Field(alias="city", default=None)

    delivery_date_begin: Optional[str] = Field(alias="delivery_date_begin", default=None)

    delivery_date_end: Optional[str] = Field(alias="delivery_date_end", default=None)

    delivery_type: Optional[str] = Field(alias="delivery_type", default=None)

    is_legal: Optional[bool] = Field(alias="is_legal", default=None)

    is_premium: Optional[bool] = Field(alias="is_premium", default=None)

    payment_type_group_name: Optional[str] = Field(alias="payment_type_group_name", default=None)

    region: Optional[str] = Field(alias="region", default=None)

    tpl_provider: Optional[str] = Field(alias="tpl_provider", default=None)

    tpl_provider_id: Optional[int] = Field(alias="tpl_provider_id", default=None)

    warehouse: Optional[str] = Field(alias="warehouse", default=None)

    warehouse_id: Optional[int] = Field(alias="warehouse_id", default=None)
