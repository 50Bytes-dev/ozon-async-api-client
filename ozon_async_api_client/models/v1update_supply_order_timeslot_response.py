from typing import *

from pydantic import BaseModel, Field

from .v1update_timeslot_error import V1updateTimeslotError


class V1updateSupplyOrderTimeslotResponse(BaseModel):
    """
    object model
    """

    errors: Optional[List[Optional[V1updateTimeslotError]]] = Field(alias="errors", default=None)

    operation_id: Optional[Union[str, int]] = Field(alias="operation_id", default=None)
