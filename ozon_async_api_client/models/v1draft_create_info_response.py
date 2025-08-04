from typing import *

from pydantic import BaseModel, Field

from .draftv1cluster import Draftv1cluster
from .v1calculation_error import V1calculationError
from .v1calculation_status import V1calculationStatus


class V1draftCreateInfoResponse(BaseModel):
    """
    None model
    """

    clusters: Optional[List[Optional[Draftv1cluster]]] = Field(alias="clusters", default=None)

    draft_id: Optional[int] = Field(alias="draft_id", default=None)

    errors: Optional[List[Optional[V1calculationError]]] = Field(alias="errors", default=None)

    status: Optional[V1calculationStatus] = Field(alias="status", default=None)
