from typing import *

from pydantic import BaseModel, Field


class V2orderVehicle(BaseModel):
    """
    object model

    Информация о водителе и автомобиле.
    """

    can_not_set_reasons: Optional[List[str]] = Field(alias="can_not_set_reasons", default=None)

    can_set: Optional[bool] = Field(alias="can_set", default=None)

    is_required: Optional[bool] = Field(alias="is_required", default=None)

    value: Optional[Any] = Field(alias="value", default=None)
