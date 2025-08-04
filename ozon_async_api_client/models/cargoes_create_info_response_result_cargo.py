from typing import *

from pydantic import BaseModel, Field

from .cargoes_create_info_response_result_cargo_value import CargoesCreateInfoResponseResultCargoValue


class CargoesCreateInfoResponseResultCargo(BaseModel):
    """
    None model
    """

    key: Optional[str] = Field(alias="key", default=None)

    value: Optional[CargoesCreateInfoResponseResultCargoValue] = Field(alias="value", default=None)
