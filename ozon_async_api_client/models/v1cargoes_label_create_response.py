from typing import *

from pydantic import BaseModel, Field

from .v1cargoes_label_create_errors import V1cargoesLabelCreateErrors


class V1cargoesLabelCreateResponse(BaseModel):
    """
    None model
    """

    operation_id: Optional[str] = Field(alias="operation_id", default=None)

    errors: Optional[V1cargoesLabelCreateErrors] = Field(alias="errors", default=None)
