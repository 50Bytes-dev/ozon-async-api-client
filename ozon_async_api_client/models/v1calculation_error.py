from typing import *

from pydantic import BaseModel, Field

from .v1items_validation import V1itemsValidation


class V1calculationError(BaseModel):
    """
    None model
    """

    error_message: Optional[str] = Field(alias="error_message", default=None)

    items_validation: Optional[List[Optional[V1itemsValidation]]] = Field(alias="items_validation", default=None)

    unknown_cluster_ids: Optional[List[str]] = Field(alias="unknown_cluster_ids", default=None)
