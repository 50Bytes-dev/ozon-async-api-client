from typing import *

from pydantic import BaseModel, Field

from .draft_supply_create_status_response_result import DraftSupplyCreateStatusResponseResult
from .v1draft_supply_create_status import V1draftSupplyCreateStatus


class V1draftSupplyCreateStatusResponse(BaseModel):
    """
    None model
    """

    error_messages: Optional[List[str]] = Field(alias="error_messages", default=None)

    result: Optional[DraftSupplyCreateStatusResponseResult] = Field(alias="result", default=None)

    status: Optional[V1draftSupplyCreateStatus] = Field(alias="status", default=None)
