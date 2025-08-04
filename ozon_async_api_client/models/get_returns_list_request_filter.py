from typing import *

from pydantic import BaseModel, Field

from .v1time_range_return_date import V1timeRangeReturnDate
from .v1time_range_storage_tariffication import V1timeRangeStorageTariffication
from .v1time_range_visual_status import V1timeRangeVisualStatus


class GetReturnsListRequestFilter(BaseModel):
    """
    object model

    Фильтры. Используйте только один фильтр в запросе: `logistic_return_date`, `storage_tariffication_start_date` или `visual_status_change_moment`, иначе вернётся ошибка.

    """

    logistic_return_date: Optional[V1timeRangeReturnDate] = Field(alias="logistic_return_date", default=None)

    storage_tariffication_start_date: Optional[V1timeRangeStorageTariffication] = Field(
        alias="storage_tariffication_start_date", default=None
    )

    visual_status_change_moment: Optional[V1timeRangeVisualStatus] = Field(
        alias="visual_status_change_moment", default=None
    )

    order_id: Optional[int] = Field(alias="order_id", default=None)

    posting_numbers: Optional[List[str]] = Field(alias="posting_numbers", default=None)

    product_name: Optional[str] = Field(alias="product_name", default=None)

    offer_id: Optional[str] = Field(alias="offer_id", default=None)

    visual_status_name: Optional[str] = Field(alias="visual_status_name", default=None)

    warehouse_id: Optional[int] = Field(alias="warehouse_id", default=None)

    barcode: Optional[str] = Field(alias="barcode", default=None)

    return_schema: Optional[str] = Field(alias="return_schema", default=None)
