from typing import *

from pydantic import BaseModel, Field


class DeliveryMethodListResponseDeliveryMethod(BaseModel):
    """
    object model
    """

    company_id: Optional[int] = Field(alias="company_id", default=None)

    created_at: Optional[str] = Field(alias="created_at", default=None)

    cutoff: Optional[str] = Field(alias="cutoff", default=None)

    id: Optional[int] = Field(alias="id", default=None)

    name: Optional[str] = Field(alias="name", default=None)

    provider_id: Optional[int] = Field(alias="provider_id", default=None)

    sla_cut_in: Optional[int] = Field(alias="sla_cut_in", default=None)

    status: Optional[str] = Field(alias="status", default=None)

    template_id: Optional[int] = Field(alias="template_id", default=None)

    updated_at: Optional[str] = Field(alias="updated_at", default=None)

    warehouse_id: Optional[int] = Field(alias="warehouse_id", default=None)
