from typing import *

from pydantic import BaseModel, Field

from .supplier_available_warehouses_response_schedule import SupplierAvailableWarehousesResponseSchedule
from .supplier_available_warehouses_response_warehouse import SupplierAvailableWarehousesResponseWarehouse


class SupplierAvailableWarehousesResponseResult(BaseModel):
    """
    object model
    """

    schedule: Optional[SupplierAvailableWarehousesResponseSchedule] = Field(alias="schedule", default=None)

    warehouse: Optional[SupplierAvailableWarehousesResponseWarehouse] = Field(alias="warehouse", default=None)
