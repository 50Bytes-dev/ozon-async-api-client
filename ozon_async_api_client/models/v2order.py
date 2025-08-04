from typing import *

from pydantic import BaseModel, Field

from .v2order_supply import V2orderSupply
from .v2order_timeslot import V2orderTimeslot
from .v2order_vehicle import V2orderVehicle
from .v2state import V2state


class V2order(BaseModel):
    """
    object model
    """

    can_cancel: Optional[bool] = Field(alias="can_cancel", default=None)

    creation_date: Optional[str] = Field(alias="creation_date", default=None)

    data_filling_deadline_utc: Optional[str] = Field(alias="data_filling_deadline_utc", default=None)

    dropoff_warehouse_id: Optional[int] = Field(alias="dropoff_warehouse_id", default=None)

    is_econom: Optional[bool] = Field(alias="is_econom", default=None)

    is_super_fbo: Optional[bool] = Field(alias="is_super_fbo", default=None)

    is_virtual: Optional[bool] = Field(alias="is_virtual", default=None)

    product_super_fbo: Optional[bool] = Field(alias="product_super_fbo", default=None)

    state: Optional[V2state] = Field(alias="state", default=None)

    supplies: Optional[List[Optional[V2orderSupply]]] = Field(alias="supplies", default=None)

    supply_order_id: Optional[int] = Field(alias="supply_order_id", default=None)

    supply_order_number: Optional[str] = Field(alias="supply_order_number", default=None)

    timeslot: Optional[V2orderTimeslot] = Field(alias="timeslot", default=None)

    vehicle: Optional[V2orderVehicle] = Field(alias="vehicle", default=None)
