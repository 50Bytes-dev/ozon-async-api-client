from typing import *

from pydantic import BaseModel, Field

from .carriage_carriage_get_response_cancel_availability import CarriageCarriageGetResponseCancelAvailability


class CarriageCarriageGetResponse(BaseModel):
    """
    None model
    """

    act_type: Optional[str] = Field(alias="act_type", default=None)

    is_waybill_enabled: Optional[bool] = Field(alias="is_waybill_enabled", default=None)

    is_econom: Optional[bool] = Field(alias="is_econom", default=None)

    arrival_pass_ids: Optional[List[int]] = Field(alias="arrival_pass_ids", default=None)

    available_actions: Optional[List[str]] = Field(alias="available_actions", default=None)

    cancel_availability: Optional[CarriageCarriageGetResponseCancelAvailability] = Field(
        alias="cancel_availability", default=None
    )

    carriage_id: Optional[int] = Field(alias="carriage_id", default=None)

    company_id: Optional[int] = Field(alias="company_id", default=None)

    containers_count: Optional[int] = Field(alias="containers_count", default=None)

    created_at: Optional[str] = Field(alias="created_at", default=None)

    delivery_method_id: Optional[int] = Field(alias="delivery_method_id", default=None)

    departure_date: Optional[str] = Field(alias="departure_date", default=None)

    first_mile_type: Optional[str] = Field(alias="first_mile_type", default=None)

    has_postings_for_next_carriage: Optional[bool] = Field(alias="has_postings_for_next_carriage", default=None)

    integration_type: Optional[str] = Field(alias="integration_type", default=None)

    is_container_label_printed: Optional[bool] = Field(alias="is_container_label_printed", default=None)

    is_partial: Optional[bool] = Field(alias="is_partial", default=None)

    partial_num: Optional[int] = Field(alias="partial_num", default=None)

    retry_count: Optional[int] = Field(alias="retry_count", default=None)

    status: Optional[str] = Field(alias="status", default=None)

    tpl_provider_id: Optional[int] = Field(alias="tpl_provider_id", default=None)

    updated_at: Optional[str] = Field(alias="updated_at", default=None)

    warehouse_id: Optional[int] = Field(alias="warehouse_id", default=None)
