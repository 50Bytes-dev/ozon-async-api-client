from typing import *

from pydantic import BaseModel, Field

from .average_delivery_time_details_request_filters_delivery_schema import \
    AverageDeliveryTimeDetailsRequestFiltersDeliverySchema
from .average_delivery_time_details_request_filters_supply_period import \
    AverageDeliveryTimeDetailsRequestFiltersSupplyPeriod


class AverageDeliveryTimeDetailsRequestFilters(BaseModel):
    """
    None model

    Фильтры.
    """

    delivery_schema: Optional[AverageDeliveryTimeDetailsRequestFiltersDeliverySchema] = Field(
        alias="delivery_schema", default=None
    )

    supply_period: Optional[AverageDeliveryTimeDetailsRequestFiltersSupplyPeriod] = Field(
        alias="supply_period", default=None
    )
