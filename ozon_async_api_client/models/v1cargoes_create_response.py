from typing import *

from pydantic import BaseModel, Field

from .v1cargoes_create_errors import V1cargoesCreateErrors


class V1cargoesCreateResponse(BaseModel):
    """
    None model
    """

    operation_id: Optional[str] = Field(alias="operation_id", default=None)

    errors: Optional[V1cargoesCreateErrors] = Field(alias="errors", default=None)
