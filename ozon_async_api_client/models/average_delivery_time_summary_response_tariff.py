from typing import *

from pydantic import BaseModel, Field

from .average_delivery_time_summary_response_tariff_status import AverageDeliveryTimeSummaryResponseTariffStatus


class AverageDeliveryTimeSummaryResponseTariff(BaseModel):
    """
    None model

    Информация о тарифе.
    """

    fee: Optional[float] = Field(alias="fee", default=None)

    start: Optional[int] = Field(alias="start", default=None)

    tariff_status: Optional[AverageDeliveryTimeSummaryResponseTariffStatus] = Field(alias="tariff_status", default=None)

    tariff_value: Optional[float] = Field(alias="tariff_value", default=None)
