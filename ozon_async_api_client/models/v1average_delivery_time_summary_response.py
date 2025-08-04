from typing import *

from pydantic import BaseModel, Field

from .average_delivery_time_summary_response_tariff import AverageDeliveryTimeSummaryResponseTariff


class V1averageDeliveryTimeSummaryResponse(BaseModel):
    """
    None model
    """

    average_delivery_time: Optional[int] = Field(alias="average_delivery_time", default=None)

    current_tariff: Optional[AverageDeliveryTimeSummaryResponseTariff] = Field(alias="current_tariff", default=None)

    lost_profit: Optional[float] = Field(alias="lost_profit", default=None)

    perfect_delivery_time: Optional[int] = Field(alias="perfect_delivery_time", default=None)

    updated_at: Optional[str] = Field(alias="updated_at", default=None)
