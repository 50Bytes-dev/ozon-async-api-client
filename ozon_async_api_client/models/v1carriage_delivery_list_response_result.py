from typing import *

from pydantic import BaseModel, Field

from .v1carriage_delivery_list_response_result_carriages import V1carriageDeliveryListResponseResultCarriages
from .v1carriage_delivery_list_response_result_errors import V1carriageDeliveryListResponseResultErrors


class V1carriageDeliveryListResponseResult(BaseModel):
    """
    object model
    """

    assembly_list_availability: Optional[bool] = Field(alias="assembly_list_availability", default=None)

    can_create_another_carriage: Optional[bool] = Field(alias="can_create_another_carriage", default=None)

    carriage_postings_count: Optional[int] = Field(alias="carriage_postings_count", default=None)

    carriage_quantum_count: Optional[int] = Field(alias="carriage_quantum_count", default=None)

    carriages: Optional[List[Optional[V1carriageDeliveryListResponseResultCarriages]]] = Field(
        alias="carriages", default=None
    )

    cut_in: Optional[str] = Field(alias="cut_in", default=None)

    delivery_method_id: Optional[int] = Field(alias="delivery_method_id", default=None)

    delivery_method_name: Optional[str] = Field(alias="delivery_method_name", default=None)

    delivery_method_status: Optional[str] = Field(alias="delivery_method_status", default=None)

    departure_date: Optional[str] = Field(alias="departure_date", default=None)

    dropoff_address: Optional[str] = Field(alias="dropoff_address", default=None)

    dropoff_change_availability: Optional[str] = Field(alias="dropoff_change_availability", default=None)

    dropoff_point_id: Optional[int] = Field(alias="dropoff_point_id", default=None)

    dropoff_point_type: Optional[str] = Field(alias="dropoff_point_type", default=None)

    errors: Optional[List[Optional[V1carriageDeliveryListResponseResultErrors]]] = Field(alias="errors", default=None)

    first_mile_changing: Optional[bool] = Field(alias="first_mile_changing", default=None)

    first_mile_type: Optional[str] = Field(alias="first_mile_type", default=None)

    has_entrusted_acceptance: Optional[bool] = Field(alias="has_entrusted_acceptance", default=None)

    integration_type: Optional[str] = Field(alias="integration_type", default=None)

    is_presort: Optional[bool] = Field(alias="is_presort", default=None)

    is_rfbs: Optional[bool] = Field(alias="is_rfbs", default=None)

    recommended_time_local: Optional[str] = Field(alias="recommended_time_local", default=None)

    recommended_time_utc_offset_in_minutes: Optional[float] = Field(
        alias="recommended_time_utc_offset_in_minutes", default=None
    )

    cutoff_at: Optional[str] = Field(alias="cutoff_at", default=None)

    mandatory_packaged_count: Optional[int] = Field(alias="mandatory_packaged_count", default=None)

    mandatory_packaged_quantum_count: Optional[int] = Field(alias="mandatory_packaged_quantum_count", default=None)

    mandatory_postings_count: Optional[int] = Field(alias="mandatory_postings_count", default=None)

    mandatory_quantum_count: Optional[int] = Field(alias="mandatory_quantum_count", default=None)

    optional_packaged_count: Optional[int] = Field(alias="optional_packaged_count", default=None)

    postings_for_another_carriage_count: Optional[int] = Field(
        alias="postings_for_another_carriage_count", default=None
    )

    quantum_for_another_carriage_count: Optional[int] = Field(alias="quantum_for_another_carriage_count", default=None)

    timeslot_from: Optional[str] = Field(alias="timeslot_from", default=None)

    timeslot_to: Optional[str] = Field(alias="timeslot_to", default=None)

    tpl_provider_icon_url: Optional[str] = Field(alias="tpl_provider_icon_url", default=None)

    tpl_provider_name: Optional[str] = Field(alias="tpl_provider_name", default=None)

    warehouse_city: Optional[str] = Field(alias="warehouse_city", default=None)

    warehouse_id: Optional[int] = Field(alias="warehouse_id", default=None)

    warehouse_name: Optional[str] = Field(alias="warehouse_name", default=None)
