from typing import *

from pydantic import BaseModel, Field

from .v1drop_off_warehouse import V1dropOffWarehouse


class V1draftTimeslotInfoResponse(BaseModel):
    """
    None model
    """

    drop_off_warehouse_timeslots: Optional[List[Optional[V1dropOffWarehouse]]] = Field(
        alias="drop_off_warehouse_timeslots", default=None
    )

    requested_date_from: Optional[str] = Field(alias="requested_date_from", default=None)

    requested_date_to: Optional[str] = Field(alias="requested_date_to", default=None)
