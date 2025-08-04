from typing import *

from pydantic import BaseModel, Field

from .seller_returnsv1money_storage import SellerReturnsv1moneyStorage
from .seller_returnsv1money_utilization import SellerReturnsv1moneyUtilization


class GetReturnsListResponseStorage(BaseModel):
    """
    object model

    Информация о хранении.
    """

    sum: Optional[SellerReturnsv1moneyStorage] = Field(alias="sum", default=None)

    tariffication_first_date: Optional[str] = Field(alias="tariffication_first_date", default=None)

    tariffication_start_date: Optional[str] = Field(alias="tariffication_start_date", default=None)

    arrived_moment: Optional[str] = Field(alias="arrived_moment", default=None)

    days: Optional[int] = Field(alias="days", default=None)

    utilization_sum: Optional[SellerReturnsv1moneyUtilization] = Field(alias="utilization_sum", default=None)

    utilization_forecast_date: Optional[str] = Field(alias="utilization_forecast_date", default=None)
