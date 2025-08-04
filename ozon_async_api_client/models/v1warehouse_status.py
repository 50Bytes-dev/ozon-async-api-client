from typing import *

from pydantic import BaseModel, Field

from .v1warehouse_scoring_invalid_reason import V1warehouseScoringInvalidReason
from .v1warehouse_scoring_status import V1warehouseScoringStatus


class V1warehouseStatus(BaseModel):
    """
    None model

    Доступность склада.
    """

    invalid_reason: Optional[V1warehouseScoringInvalidReason] = Field(alias="invalid_reason", default=None)

    is_available: Optional[bool] = Field(alias="is_available", default=None)

    state: Optional[V1warehouseScoringStatus] = Field(alias="state", default=None)
