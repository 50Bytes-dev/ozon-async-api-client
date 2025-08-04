from typing import *

from pydantic import BaseModel, Field

from .v2posting_fbsact_list_related_docs import V2postingFBSActListRelatedDocs


class V2postingFBSActListResult(BaseModel):
    """
    object model
    """

    id: Optional[int] = Field(alias="id", default=None)

    delivery_method_id: Optional[int] = Field(alias="delivery_method_id", default=None)

    delivery_method_name: Optional[str] = Field(alias="delivery_method_name", default=None)

    integration_type: Optional[str] = Field(alias="integration_type", default=None)

    containers_count: Optional[int] = Field(alias="containers_count", default=None)

    status: Optional[str] = Field(alias="status", default=None)

    departure_date: Optional[str] = Field(alias="departure_date", default=None)

    created_at: Optional[str] = Field(alias="created_at", default=None)

    updated_at: Optional[str] = Field(alias="updated_at", default=None)

    act_type: Optional[str] = Field(alias="act_type", default=None)

    is_partial: Optional[bool] = Field(alias="is_partial", default=None)

    has_postings_for_next_carriage: Optional[bool] = Field(alias="has_postings_for_next_carriage", default=None)

    partial_num: Optional[int] = Field(alias="partial_num", default=None)

    related_docs: Optional[V2postingFBSActListRelatedDocs] = Field(alias="related_docs", default=None)
