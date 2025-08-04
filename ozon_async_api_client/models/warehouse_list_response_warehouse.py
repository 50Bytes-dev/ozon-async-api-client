from typing import *

from pydantic import BaseModel, Field

from .warehouse_first_mile_type import WarehouseFirstMileType


class WarehouseListResponseWarehouse(BaseModel):
    """
    object model
    """

    has_entrusted_acceptance: Optional[bool] = Field(alias="has_entrusted_acceptance", default=None)

    is_rfbs: Optional[bool] = Field(alias="is_rfbs", default=None)

    name: Optional[str] = Field(alias="name", default=None)

    warehouse_id: Optional[int] = Field(alias="warehouse_id", default=None)

    can_print_act_in_advance: Optional[bool] = Field(alias="can_print_act_in_advance", default=None)

    first_mile_type: Optional[WarehouseFirstMileType] = Field(alias="first_mile_type", default=None)

    has_postings_limit: Optional[bool] = Field(alias="has_postings_limit", default=None)

    is_karantin: Optional[bool] = Field(alias="is_karantin", default=None)

    is_kgt: Optional[bool] = Field(alias="is_kgt", default=None)

    is_economy: Optional[bool] = Field(alias="is_economy", default=None)

    is_timetable_editable: Optional[bool] = Field(alias="is_timetable_editable", default=None)

    min_postings_limit: Optional[int] = Field(alias="min_postings_limit", default=None)

    postings_limit: Optional[int] = Field(alias="postings_limit", default=None)

    min_working_days: Optional[int] = Field(alias="min_working_days", default=None)

    status: Optional[str] = Field(alias="status", default=None)

    working_days: Optional[Any] = Field(alias="working_days", default=None)
