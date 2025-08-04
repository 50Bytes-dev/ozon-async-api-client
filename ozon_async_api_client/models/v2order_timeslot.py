from typing import *

from pydantic import BaseModel, Field

from .v2timeslot_zoned_message import V2timeslotZonedMessage


class V2orderTimeslot(BaseModel):
    """
    object model

    Интервал поставки.
    """

    can_not_set_reasons: Optional[List[str]] = Field(alias="can_not_set_reasons", default=None)

    can_set: Optional[bool] = Field(alias="can_set", default=None)

    is_required: Optional[bool] = Field(alias="is_required", default=None)

    value: Optional[V2timeslotZonedMessage] = Field(alias="value", default=None)
