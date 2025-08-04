from typing import *

from pydantic import BaseModel, Field

from .v1cargoes_label_create_request_cargo import V1cargoesLabelCreateRequestCargo


class V1cargoesLabelCreateRequest(BaseModel):
    """
    None model
    """

    cargoes: Optional[List[Optional[V1cargoesLabelCreateRequestCargo]]] = Field(alias="cargoes", default=None)

    supply_id: int = Field(alias="supply_id")
