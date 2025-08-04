from typing import *

from pydantic import BaseModel, Field


class V2orderSupplySupplyTags(BaseModel):
    """
    object model
    """

    is_ettn_required: Optional[bool] = Field(alias="is_ettn_required", default=None)

    is_evsd_required: Optional[bool] = Field(alias="is_evsd_required", default=None)

    is_jewelry: Optional[bool] = Field(alias="is_jewelry", default=None)

    is_marking_possible: Optional[bool] = Field(alias="is_marking_possible", default=None)

    is_marking_required: Optional[bool] = Field(alias="is_marking_required", default=None)

    is_traceable: Optional[bool] = Field(alias="is_traceable", default=None)
