from typing import *

from pydantic import BaseModel, Field

from .v1cargoes_create_request_cargo import V1cargoesCreateRequestCargo


class V1cargoesCreateRequest(BaseModel):
    """
    None model
    """

    cargoes: List[V1cargoesCreateRequestCargo] = Field(alias="cargoes")

    delete_current_version: Optional[bool] = Field(alias="delete_current_version", default=None)

    supply_id: int = Field(alias="supply_id")
