from typing import *

from pydantic import BaseModel, Field

from .v1cargoes_create_request_cargo_value import V1cargoesCreateRequestCargoValue


class V1cargoesCreateRequestCargo(BaseModel):
    """
    None model
    """

    key: str = Field(alias="key")

    value: V1cargoesCreateRequestCargoValue = Field(alias="value")
