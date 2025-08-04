from typing import *

from pydantic import BaseModel, Field

from .v1posting_fbs_timeslot_change_restrictions_delivery_interval import \
    V1postingFbsTimeslotChangeRestrictionsDeliveryInterval


class V1postingFbsTimeslotChangeRestrictionsResponse(BaseModel):
    """
    object model
    """

    delivery_interval: Optional[V1postingFbsTimeslotChangeRestrictionsDeliveryInterval] = Field(
        alias="delivery_interval", default=None
    )

    remaining_changes_count: Optional[int] = Field(alias="remaining_changes_count", default=None)
