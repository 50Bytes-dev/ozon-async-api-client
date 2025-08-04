from typing import *

from pydantic import BaseModel, Field


class GetCarriageAvailableListResponseResult(BaseModel):
    """
    object model
    """

    carriage_id: Optional[int] = Field(alias="carriage_id", default=None)

    carriage_postings_count: Optional[int] = Field(alias="carriage_postings_count", default=None)

    carriage_status: Optional[str] = Field(alias="carriage_status", default=None)

    cutoff_at: Optional[str] = Field(alias="cutoff_at", default=None)

    delivery_method_id: Optional[int] = Field(alias="delivery_method_id", default=None)

    delivery_method_name: Optional[str] = Field(alias="delivery_method_name", default=None)

    errors: Optional[Any] = Field(alias="errors", default=None)

    first_mile_type: Optional[str] = Field(alias="first_mile_type", default=None)

    has_entrusted_acceptance: Optional[bool] = Field(alias="has_entrusted_acceptance", default=None)

    mandatory_postings_count: Optional[int] = Field(alias="mandatory_postings_count", default=None)

    mandatory_packaged_count: Optional[int] = Field(alias="mandatory_packaged_count", default=None)

    recommended_time_local: Optional[str] = Field(alias="recommended_time_local", default=None)

    recommended_time_utc_offset_in_minutes: Optional[float] = Field(
        alias="recommended_time_utc_offset_in_minutes", default=None
    )

    tpl_provider_icon_url: Optional[str] = Field(alias="tpl_provider_icon_url", default=None)

    tpl_provider_name: Optional[str] = Field(alias="tpl_provider_name", default=None)

    warehouse_city: Optional[str] = Field(alias="warehouse_city", default=None)

    warehouse_id: Optional[int] = Field(alias="warehouse_id", default=None)

    warehouse_name: Optional[str] = Field(alias="warehouse_name", default=None)

    warehouse_timezone: Optional[str] = Field(alias="warehouse_timezone", default=None)
